"""
graph_stats.py
Computes usage statistics of vocabulary terms in research.md and produces
graph_data.json used by vocabulary_graph.html.

Two frequency types are calculated separately:
  - explicit: the term itself (or its direct spelling variants) appears in the text
  - implicit: the concept is used without naming the term (synonyms / related phrases)
"""
import json
import re
from pathlib import Path

REPORT = Path(__file__).parent / "research.md"

# Sections of the report (## headings) used as graph nodes
SECTIONS = ["Healthcare", "Finance", "Cyber Security", "Virtual Assistants", "Content Creation"]

# term -> {"explicit": [regexes], "implicit": [regexes]}
# regexes are case-insensitive; use groups (?:) to avoid capture artifacts
TERMS = {
    "Synthetic data": {
        "explicit": [r"synthetic data", r"\[synthetic\]"],
        "implicit": [r"synthetic (?:images|medical imaging)", r"AI-generated images",
                     r"produce synthetic images", r"generate synthetic"],
    },
    "GAN": {
        "explicit": [r"\bGANs?\b", r"generative adversarial networks? \(GANs?\)", r"conditional GANs", r"EBGAN"],
        "implicit": [r"adversarial auto-encoders", r"adversarial techniques", r"two competing AI models",
                     r"competing networks"],
    },
    "Foundation model": {
        "explicit": [r"foundation models?"],
        "implicit": [r"general representation", r"general intelligence"],
    },
    "Fine-tuning": {
        "explicit": [r"fine-tun(?:e|ed|ing)"],
        "implicit": [r"\badapt(?:ed|ing)?\b"],
    },
    "EHR": {
        "explicit": [r"\bEHRs?\b", r"electronic health records?"],
        "implicit": [r"medical records?", r"clinical documentation", r"unstructured clinical"],
    },
    "PII": {
        "explicit": [r"personal identifiable information", r"\bPII\b"],
        "implicit": [r"\bHIPAA\b", r"privacy"],
    },
    "Model bias": {
        "explicit": [r"\bmodel bias\b", r"biased outputs?", r"data bias", r"biased input data"],
        "implicit": [r"inequalities"],
    },
    "Explainability": {
        "explicit": [r"explainability"],
        "implicit": [r"transparency"],
    },
    "Transformer": {
        "explicit": [r"transformers?"],
        "implicit": [r"self-attention", r"attention mechanism"],
    },
    "GPT": {
        "explicit": [r"\bGPT\b"],
        "implicit": [r"OpenAI"],
    },
    "NLP": {
        "explicit": [r"natural language processing(?: \(NLP\))?", r"\bNLP\b"],
        "implicit": [r"human-like language", r"human-like interaction", r"plain-language",
                     r"natural, contextually relevant", r"radiologist-style language"],
    },
    "Data augmentation": {
        "explicit": [r"data augmentation", r"\baugment(?:ed|ing|s)?\b"],
        "implicit": [r"\bdatasets?\b"],
    },
    "De-identification": {
        "explicit": [r"de-identif(?:y|ication|ied)"],
        "implicit": [r"not representing real patients", r"synthetic images that preserve key clinical features"],
    },
    "Model drift": {
        "explicit": [r"model drift"],
        "implicit": [r"environment changes", r"models? learn as the environment", r"context shifts"],
    },
    "Human-in-the-loop": {
        "explicit": [r"human-in-the-loop"],
        "implicit": [r"human element", r"human expertise", r"developers validate", r"radiologists?",
                     r"security-?ops team", r"human oversight"],
    },
    "Deep learning": {
        "explicit": [r"deep learning"],
        "implicit": [r"non-linear correlations", r"neural networks?"],
    },
    "Prompt": {
        "explicit": [r"\bprompts?\b"],
        "implicit": [r"plain-language question", r"simple prompts"],
    },
    "Chatbot": {
        "explicit": [r"chatbots?", r"conversational AI systems"],
        "implicit": [r"conversational finance", r"simulates? conversation"],
    },
    "Virtual assistant": {
        "explicit": [r"virtual assistants?", r"virtual financial assistant", r"AI Tutor", r"AI Assistant",
                     r"intelligence co-analyst"],
        "implicit": [r"Erica", r"Alexa", r"Duolingo"],
    },
    "Anomaly detection": {
        "explicit": [r"anomaly detection", r"anomal(?:y|ies)"],
        "implicit": [r"unusual spikes", r"novel or stealthy threats", r"deviat(?:e|ion|ions)", r"anomalous"],
    },
}


def count(patterns: list[str], text: str) -> int:
    spans = sorted(
        match.span()
        for pattern in patterns
        for match in re.finditer(pattern, text, flags=re.IGNORECASE)
    )
    merged = []
    for start, end in spans:
        if merged and start < merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    return len(merged)


def split_sections(text: str) -> dict[str, str]:
    """Split report into the 5 top-level sections."""
    # cut everything before the first section heading
    parts = re.split(r"^## (.+)$", text, flags=re.MULTILINE)
    # parts = [intro, name1, body1, name2, body2, ...]
    sections = {}
    for i in range(1, len(parts) - 1, 2):
        name = parts[i].strip()
        body = parts[i + 1]
        # normalize section names to our canonical list
        for canon in SECTIONS:
            if name.lower().startswith(canon.split()[0].lower()):
                sections[canon] = sections.get(canon, "") + body
    return sections


def main():
    text = REPORT.read_text(encoding="utf-8")
    # strip markdown links targets but keep visible text
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    sections = split_sections(text)

    nodes, links, stats = [], [], []

    for term, pats in TERMS.items():
        e_total = count(pats["explicit"], text)
        i_total = count(pats["implicit"], text)
        stats.append({"term": term, "explicit": e_total, "implicit": i_total})
        nodes.append({"id": term, "type": "term", "explicit": e_total, "implicit": i_total})

    for sec, body in sections.items():
        nodes.append({"id": sec, "type": "section", "explicit": 0, "implicit": 0})
        for term, pats in TERMS.items():
            e = count(pats["explicit"], body)
            i = count(pats["implicit"], body)
            if e + i > 0:
                links.append({"source": term, "target": sec, "explicit": e, "implicit": i})

    # term-term co-occurrence: terms used in the same section
    term_ids = list(TERMS.keys())
    for a in range(len(term_ids)):
        for b in range(a + 1, len(term_ids)):
            w = 0
            for body in sections.values():
                if count(TERMS[term_ids[a]]["explicit"] + TERMS[term_ids[a]]["implicit"], body) > 0 and \
                   count(TERMS[term_ids[b]]["explicit"] + TERMS[term_ids[b]]["implicit"], body) > 0:
                    w += 1
            if w > 0:
                links.append({"source": term_ids[a], "target": term_ids[b], "explicit": 0, "implicit": 0,
                              "cooc": w})

    data = {"nodes": nodes, "links": links, "stats": stats}
    out = Path(__file__).parent / "graph_data.json"
    out.write_text(json.dumps(data, indent=2), encoding="utf-8")
    # JS variant for vocabulary_graph.html (classic <script src> works on file://)
    js = Path(__file__).parent / "graph_data.js"
    js.write_text("const DATA = " + json.dumps(data, indent=2) + ";\n", encoding="utf-8")

    print(f"{'term':<22} {'explicit':>8} {'implicit':>8}")
    for s in stats:
        print(f"{s['term']:<22} {s['explicit']:>8} {s['implicit']:>8}")
    print(f"\nlinks: {len(links)}  ->  written to {out.name}")


if __name__ == "__main__":
    main()
