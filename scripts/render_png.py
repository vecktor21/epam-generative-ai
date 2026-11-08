"""
render_png.py
Renders a static PNG bipartite graph from graph_data.json.
Sections are on the left, all vocabulary terms are in a labeled center column,
and the table on the right shows explicit and implicit frequency for every term.
"""
import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch

DIR = Path(__file__).parent
DATA = json.loads((DIR / "graph_data.json").read_text(encoding="utf-8"))

W, H = 26.0, 19.0
C_BG, C_PANEL = "#0f1420", "#171e2e"
C_TEXT, C_MUTED = "#e8ecf4", "#93a0b8"
C_TERM, C_SEC, C_IMP = "#4da3ff", "#ffb454", "#6ee7b7"

nodes = {n["id"]: n for n in DATA["nodes"]}
terms = [n for n in DATA["nodes"] if n["type"] == "term"]
sections = [n for n in DATA["nodes"] if n["type"] == "section"]
usage = [l for l in DATA["links"] if "cooc" not in l]

# Fixed bipartite layout: five section hubs on the left, every vocabulary term
# on its own row in the middle, usage counts in a table on the right.
section_x = 2.25
term_x = 9.0
top_y, bottom_y = 16.7, 1.35
term_gap = (top_y - bottom_y) / (len(terms) - 1)
for i, n in enumerate(terms):
    n["x"] = term_x
    n["y"] = top_y - i * term_gap
section_top, section_bottom = 14.9, 3.15
section_gap = (section_top - section_bottom) / (len(sections) - 1)
for i, n in enumerate(sections):
    n["x"] = section_x
    n["y"] = section_top - i * section_gap

max_edge = max(max(l["explicit"], l["implicit"]) for l in usage) or 1

fig = plt.figure(figsize=(W, H), facecolor=C_BG)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.axis("off")
ax.set_facecolor(C_BG)

# Header
ax.text(0.55, H - 0.52, "GenAI Vocabulary — Usage Relationship Graph",
        ha="left", va="top", fontsize=23, fontweight="bold", color=C_TEXT)
ax.text(0.58, H - 1.15,
        "Vocabulary terms linked to the report sections where they appear or are used implicitly.",
        ha="left", va="top", fontsize=12.5, color=C_MUTED)

# Subtle panel backplates for graph and frequency table
ax.add_patch(plt.Rectangle((0.35, 0.55), 12.25, 16.65,
                           facecolor=C_PANEL, edgecolor="#2a3550", lw=1.0, zorder=0))
ax.add_patch(plt.Rectangle((13.0, 0.55), 12.6, 16.65,
                           facecolor=C_PANEL, edgecolor="#2a3550", lw=1.0, zorder=0))
ax.text(0.68, 16.9, "REPORT SECTIONS", color=C_MUTED, fontsize=10.5, fontweight="bold")
ax.text(7.3, 16.9, "VOCABULARY TERMS", color=C_MUTED, fontsize=10.5, fontweight="bold")

# Draw separate links for explicit and implicit matches, slightly curved apart.
for link in usage:
    s, t = nodes[link["source"]], nodes[link["target"]]
    for amount, color, rad, style, alpha in (
        (link["explicit"], C_TERM, 0.065, "solid", 0.78),
        (link["implicit"], C_IMP, -0.065, (0, (4, 3)), 0.72),
    ):
        if amount == 0:
            continue
        ax.add_patch(FancyArrowPatch(
            (s["x"] + 0.47, s["y"]), (t["x"] - 0.25, t["y"]),
            connectionstyle=f"arc3,rad={rad}", arrowstyle="-",
            color=color, lw=0.75 + 2.8 * amount / max_edge,
            linestyle=style, alpha=alpha, zorder=1,
        ))

# Section hubs and labels
for s in sections:
    ax.add_patch(plt.Circle((s["x"], s["y"]), 0.48, facecolor=C_SEC,
                            edgecolor="#8a5a1a", lw=1.8, zorder=3))
    ax.text(s["x"], s["y"] - 0.77, s["id"], ha="center", va="top",
            fontsize=12, fontweight="bold", color=C_SEC, zorder=4)

# Every vocabulary term gets a clearly labeled node on its own row.
max_total = max(n["explicit"] + n["implicit"] for n in terms) or 1
for n in terms:
    total = n["explicit"] + n["implicit"]
    radius = 0.12 + 0.12 * total / max_total
    ax.add_patch(plt.Circle((n["x"], n["y"]), radius, facecolor=C_TERM,
                            alpha=0.95, edgecolor="#1c5aa0", lw=1.2, zorder=3))
    ax.text(n["x"] + 0.38, n["y"], n["id"], ha="left", va="center",
            fontsize=10.5, color=C_TEXT, zorder=4)

# Frequency table for all terms, sorted by total count to aid scanning.
stats = sorted(DATA["stats"], key=lambda s: (-(s["explicit"] + s["implicit"]), s["term"]))
tx = 13.45
ax.text(tx, 16.85, "USAGE FREQUENCIES IN REPORT", ha="left", va="center",
        fontsize=13, fontweight="bold", color=C_MUTED)
header_y = 16.18
ax.text(tx, header_y, "Vocabulary term", ha="left", va="center",
        fontsize=10.5, fontweight="bold", color=C_MUTED)
ax.text(22.55, header_y, "Explicit", ha="right", va="center",
        fontsize=10.5, fontweight="bold", color=C_TERM)
ax.text(23.95, header_y, "Implicit", ha="right", va="center",
        fontsize=10.5, fontweight="bold", color=C_IMP)
ax.text(25.2, header_y, "Total", ha="right", va="center",
        fontsize=10.5, fontweight="bold", color=C_MUTED)

row_top, row_gap = 15.48, 0.70
for i, s in enumerate(stats):
    y = row_top - i * row_gap
    if i % 2 == 0:
        ax.add_patch(plt.Rectangle((13.3, y - 0.28), 11.95, 0.56,
                                   facecolor="#1c2438", edgecolor="none", zorder=0.5))
    ax.text(tx, y, s["term"], ha="left", va="center", fontsize=10.5, color=C_TEXT, zorder=2)
    ax.text(22.55, y, str(s["explicit"]), ha="right", va="center", fontsize=10.5,
            color=C_TERM, zorder=2)
    ax.text(23.95, y, str(s["implicit"]), ha="right", va="center", fontsize=10.5,
            color=C_IMP, zorder=2)
    ax.text(25.2, y, str(s["explicit"] + s["implicit"]), ha="right", va="center",
            fontsize=10.5, fontweight="bold", color=C_TEXT, zorder=2)

# Legend / counting note
legend = [
    Line2D([], [], color=C_TERM, lw=2.6, label="Explicit: term named in section"),
    Line2D([], [], color=C_IMP, lw=2.6, linestyle=(0, (4, 3)),
           label="Implicit: related phrase / synonym in section"),
    Line2D([], [], marker="o", color="none", markerfacecolor=C_SEC, markersize=10,
           label="Report section"),
    Line2D([], [], marker="o", color="none", markerfacecolor=C_TERM, markersize=8,
           label="Vocabulary term (size indicates total usage)"),
]
leg = ax.legend(handles=legend, loc="lower left", bbox_to_anchor=(0.02, 0.005),
                frameon=True, fontsize=9.5, ncol=2, labelcolor=C_TEXT,
                columnspacing=1.8, handlelength=2.4)
leg.get_frame().set_facecolor(C_PANEL)
leg.get_frame().set_edgecolor("#2a3550")

ax.text(13.45, 1.0,
        "Counts are regex-based. Implicit phrase matches are approximate and use curated patterns.",
        ha="left", va="center", fontsize=9.5, color=C_MUTED)

out = DIR / "vocabulary_graph.png"
fig.savefig(out, dpi=140, facecolor=C_BG)
plt.close(fig)
print(f"Saved {out}")
