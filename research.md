Generative AI is used in wide number of areas, including: healthcare, finance, entertainment and media, cyber security, education, gaming, virtual assistants, content creation.

## Healthcare

#### Healthcare Delivery

Use cases in healthcare is used in these areas: healthcare delivery, healthcare administration, population health, public health initiatives, research and development
Use cases in healthcare delivery:

##### Synthetic medical imaging:

Generative AI, especially Generative Adversarial Networks (GANs), can be trained to generate synthetic medical images that mimic real-world X-rays, MRIs, and CT scans. These [synthetic](https://aimultiple.com/synthetic-data-use-cases) images have several important applications in healthcare:

* **Medical training & education:** AI-generated images can be used to train healthcare professionals by creating diverse datasets of rare diseases, anomalies, or normal variants that may not always be present in real-world cases.
* **Data augmentation for AI models: **Training AI systems to diagnose medical conditions requires large datasets. Generative AI can produce synthetic images to augment limited datasets, thereby improving the accuracy of diagnostic models without compromising privacy.
* **Simulation and research:** Synthetic images can help researchers simulate various scenarios (such as how a disease might progress) or test AI algorithms without waiting for new patient data. This process can support accelerating medical research.
* **De-identification of data:** By generating synthetic images that preserve key clinical features while not representing real patients, healthcare systems can share data without violating privacy laws such as HIPAA.

Some list of GAN tools\frameworks for synthetic data generation:

1) pygan (python library, https://pypi.org/project/pygan/)
   pygan is Python library to implement Generative Adversarial Networks(GANs), Conditional GANs, Adversarial Auto-Encoders(AAEs), and Energy-based Generative Adversarial Network(EBGAN).
2) TF-GAN (python library, https://www.tensorflow.org/tutorials/generative/dcgan) - Tensorflow GANs, also known as TF- GAN, is an open-source lightweight Python library. Google AI researchers developed it for the easy and effective implementation of GANs.

##### Generate personalized treatment plans

Generative AI models can analyze a patient’s comprehensive medical history, genetic profile, lifestyle factors, and even real-time health data (e.g., from wearables such as smartwatches) to create personalized treatment plans. Here’s how this works:

* **Patient analysis: **AI systems can identify patterns in a patient’s history, such as past diagnoses, treatment responses, and genetic predispositions. Generative AI tools can then generate a treatment plan tailored to the patient’s unique circumstances.
* **Integrating real-time data: **AI can pull in data from sources such as wearable devices, lab tests, and continuous monitoring systems. Based on this data, the system can adjust or generate new treatment recommendations to ensure the patient is always on the most effective course of treatment.
* **Predictive treatment: **By generating models that simulate how a patient might respond to various treatments, generative AI tools can suggest options that maximize the likelihood of success. For example, if a patient has a specific genetic mutation associated with a poor response to a drug, these tools could suggest alternatives beforehand.
* **Automating complex decision-making: **Complex conditions such as cancer often require multi-modal treatments involving surgery, chemotherapy, and targeted therapies. Generative AI tools can assist by creating treatment schedules, predicting side effects, and coordinating multi-disciplinary care tailored to the patient’s evolving condition.
* **Personalized medication: **AI can recommend personalized dosages or [medication](https://aimultiple.com/drug-discovery-software) types based on the patient’s metabolic profile, reducing the risk of adverse drug reactions or inefficient treatments.

###### Real-life examples:

1) Google Research’s SensorFM (https://research.google/blog/sensorfm-towards-a-general-intelligence-and-interface-for-wearable-health-data/) Google Research introduced SensorFM, a foundation model designed to convert continuous wearable-sensor data into health-related insights. SensorFM learns a general representation of human physiology that can be adapted to cardiovascular, metabolic, sleep, mental-health, lifestyle, and demographic tasks.
2) Mayo Clinic with Cerebras Systems (https://www.fiercehealthcare.com/health-tech/jpm24-mayo-clinic-deepens-ai-commitment-new-cerebras-systems-deal): In 2024, Mayo Clinic partnered with Cerebras Systems to develop AI models that analyze genomic data from over 100,000 patients. These models aim to predict individual responses to treatments, such as assessing the efficacy of methotrexate in rheumatoid arthritis patients, enabling more tailored therapeutic strategies

##### Medical record analysis

Generative AI models in healthcare settings can extract insights from unstructured clinical documentation, such as EHRs and CT scans. This improves diagnostic accuracy and healthcare providers’ ability to make informed decisions.

The technology also holds promise in analyzing medical conditions and clinical trials by using training data to fine-tune models in a controlled environment.

###### Real-life example: Harrison.ai’s Harrison.Rad 1.5 (https://harrison.ai/radiology-foundation-model/):

Harrison.ai introduced Harrison.Rad 1.5, a radiology-specific foundation model designed to generate structured draft reports from medical images, prior studies, and clinical context.

The model can support radiologists by:

* **Drafting radiology reports: **Analyzes imaging data and generates structured report drafts in radiologist-style language.
* **Comparing prior scans:** Can evaluate current imaging against previous studies and describe interval changes.
* **Localizing anatomical findings:** Identifies findings with greater anatomical specificity and can include measurements such as cardiothoracic ratio.
* **Handling complex cases:** Designed to reason across multi-finding studies, including chest, abdomen, musculoskeletal, spine, and emergency imaging cases.
* **Adapting report style: **Can adjust reporting language based on the clinical question and case context.

#### Challenges and Considerations for Responsible Adoption

In spite of the considerable potential for generative AIs to be used in healthcare delivery settings, some obstacles must be surmounted before this technology can be adopted responsibly and successfully. The following are what organizations should take into consideration:

* **Data Privacy and Security While Using Generative Models: ***Personal identifiable information (PII)* is present in large data sets that are used to train generative models. It is vital that these datasets are protected from unauthorized access or misuse, thereby making them secure. **This calls for robust governance structures on data protection, as well as stringent regulations protecting patient privacy rights.**
* **Model Bias & Explainability: **Biased outputs may result when generative models learn from biased input data such as historical medical records characterized by inequalities among different population groups. In order to foster transparency so that end-users can appreciate the decision-making process of an** AI system** about a particular case.
* **Legal Frameworks:** There is still no established legal framework governing the use of artificial intelligence in healthcare. Thus, there should exist clear guidelines which will ensure safety, efficacy and ethicality while using such tools in clinical settings.
* **Impacts on workforce: **Though it may help streamline activities within hospitals thereby improving efficiency levels; there needs consideration given regarding possible effects brought about by this innovation towards staff members involved directly or indirectly with patient care provision. **This will call for re-skilling programs among nurses, doctors and other healthcare workers.**

## Finance

Generative AI is transforming the finance industry by assisting with fraud detection, creating customized investment plans, and improving risk management

### Finance functions in non-financial firms

#### 1-Automation of accounting functions

Specialized transformer models help finance units automate functions such as auditing and accounts payable, including invoice capture and processing. With deep learning functions, [GPT](https://aimultiple.com/gpt-5) models specialized in accounting can achieve high rates of automation in most accounting tasks.

### Financial services firms

#### 2-Conversational finance

[Generative AI](https://aimultiple.com/generative-ai-applications) models can produce more natural, contextually relevant responses because they are trained to understand and generate human-like language patterns. As a result, generative AI can significantly enhance the performance and user experience of financial conversational AI systems and chatbots by providing more accurate, engaging, and nuanced interactions with users.

Conversational finance provides customers with:

* Improved customer support
* Personalized financial advice
* Payment notifications
* Document generation, such as investment summaries or loan applications.

For instance, [Morgan Stanley employs OpenAI-powered chatbots](https://openai.com/index/morgan-stanley/) to support financial advisors by leveraging the company’s internal research and data as a knowledge resource.


### Back office

#### 4-Code Modernization for Legacy Systems

Banks still run software written in COBOL from the 1970s and 80s. Finding developers who know COBOL is nearly impossible, but this software handles critical transactions and can’t just be turned off.

Generative AI models can:

* Read legacy code in COBOL, Fortran, or other old languages
* Convert it to modern languages like Python or Java
* Maintain the same business logic while improving performance
* Generate documentation explaining what the code actually does

Goldman Sachs confirmed that generative AI is now central to its application development and enhancement efforts. One bank’s developers validate AI-generated code, catching errors before deployment, but the AI does the heavy lifting.

Technology costs make up \~10% of a typical bank’s expenses. Speeding up development and reducing maintenance costs directly improves profitability.[<sup>3</sup>](https://aimultiple.com/generative-ai-finance#easy-footnote-bottom-3-66514 "Michael Abbott (May 8, 2023).”What Generative AI Means For Banking“. Forbes")

#### 5-Application modernization

Banks aim to avoid relying on outdated software and are continually investing in modernization efforts. [Enterprise GenAI models can convert code from legacy software languages to modern ones, enabling developers to validate the new software and](https://aimultiple.com/enterprise-generative-ai) saving significant time.

Employees at Goldman Sachs confirm that generative AI is a strong aspect of application development and enhancement.[<sup>4</sup>](https://aimultiple.com/generative-ai-finance#easy-footnote-bottom-4-66514 "“Goldman Sachs Deploys Its First Generative AI Tool Across the Firm”. Wall Street Journal")

#### 6-Automated Document Generation

Banks produce thousands of documents daily: investment summaries, loan applications, client reports, and regulatory submissions. These documents pull from templates, but customizing them takes time.

Generative AI now handles this:

* Generate professional documents from simple prompts
* Pull relevant data from multiple systems
* Apply appropriate formatting based on document type and recipient

## Cyber Security

Generative AI is revolutionizing cybersecurity by improving threat detection and automating incident response. Generative AI is reshaping[ cybersecurity](https://www.geeksforgeeks.org/ethical-hacking/what-is-cyber-security/) by proactively identifying threats, simulating attack scenarios, and enhancing incident response capabilities. Below are some few applications of Generative AI in Cyber Security.

* **Anomaly Detection:** Generative AI analyzes large datasets to identify patterns of normal behavior within a network. For instance, it can detect unusual spikes in network traffic that may indicate a malware attack or unauthorized access.
* **Phishing Detection:** Advanced phishing attacks can be countered through generative AI by[ natural language processing (NLP)](https://www.geeksforgeeks.org/nlp/natural-language-processing-nlp-tutorial/), analyzing the content of emails and social media communications to look for slight anomalies of false activities.
* **Incident Analysis and Prioritization:** Generative AI can automatically analyze security incidents in real time, prioritize them based on severity, and allow the security team to respond accordingly.
* **Proactive Vulnerability and Attack-Surface Management**. AI helps identify vulnerabilities before they’re exploited. For example, one [review](https://www.sciencedirect.com/science/article/pii/S1566253523001136?) emphasised how AI-driven tools map data flows, user behaviours, and vendor scripts to highlight weak spots.
* **Adaptive Learning for Emerging Threats:** When properly maintained, AI models learn as the environment changes. A key research survey pointed out that deep learning’s ability to uncover “complex, non-linear correlations” is precisely what enables the detection of novel or stealthy threats. However, and this is important, the human element remains. AI must be trained, tuned, and monitored; false positives, model drift, and context shifts are real. Implement regular model validation and feedback loops. Your security-ops team should review AI alerts to refine the model and reduce noise over time.

#### Cautions and Considerations

While the benefits are substantial, research reminds us of limits and risks. For instance, there is growing scrutiny on AI-enabled adversarial techniques and how attackers might use AI to bypass defences.

Data bias, explainability, and integration into legacy systems are additional challenges. [One paper](https://arxiv.org/abs/2401.01342?) noted that successful deployment of AI in cybersecurity requires not just the model but also the broader infrastructure and processes that support it.

Treat AI as a strategic capability, not a plug-and-play magic bullet. Ensure your organization has the governance, data hygiene, and human-in-the-loop oversight to derive value from AI safely.

### Example: Group IB Smart AI Assistant

At Group-IB, our mission has always been to give defenders the upper hand by simplifying complexity and amplifying human expertise. The [Group-IB Smart AI Assistant](https://www.group-ib.com/blog/smart-ai-assistant/) is the next step in that journey: a tool built not to replace analysts, but to empower them with immediate, evidence-based clarity.

Our AI Assistant works as an intelligence co-analyst, translating years of threat data, research, and contextual understanding into real-time, actionable answers. Ask it a plain-language question, about a threat actor, a phishing domain, a recent malware variant, and it responds with the same structured precision you’d expect from a seasoned analyst. The difference? It happens in seconds, not hours.


## Virtual Assistants

AI-powered chatbots use generative models to provide a more human-like interaction with customers in customer service scenarios, answering queries and resolving issues effectively.

* **Erica (Bank of America): **Erica is a virtual financial assistant that assists over 25 million users in managing their accounts, paying bills, and getting spending insights, making banking more accessible and efficient.
* **Amazon Alexa: **Alexa provides personalized product recommendations based on user preferences and past purchases, making shopping easier for millions of customers.
* **Duolingo's AI Tutor:** Duolingo employs a virtual assistant to tailor language lessons to the user's progress. It provides real-time feedback and gamified learning experiences.

## Content Creation

Generative AI is revolutionizing content creation across various industries. From text and images to videos and music, AI-powered tools streamline workflows, boost creativity, and enhance productivity while ensuring consistency and scalability.** **Below are the key applications of Generative AI in Content Creation

* **Netflix:** Uses AI algorithms to analyze viewing habits and preferences, providing personalized recommendations that enhance user engagement. This personalization accounts for 80% of the content streamed on the platform.
* **Sephora:** It uses an augmented reality application called "Virtual Artist," which enables the user to try makeup products virtually, so the shopping experience is further enhanced through personal interactions with the product.
* **StoryChief:** AI is a system that helps in the production of blog articles, full with headings and SEO metadata, to assist writers get over writer's block and save time in content creation.

## Used literature:

1) Generative AI Applications [https://www.geeksforgeeks.org/artificial-intelligence/generative-ai-applications/]
2) Impact of Generative AI in Health Care [https://www.geeksforgeeks.org/blogs/impact-of-generative-ai-in-health-care/]
3) 17 Generative AI Healthcare Use Cases [https://aimultiple.com/generative-ai-healthcare]
4) Top 25 Generative AI Finance Use Cases [https://aimultiple.com/generative-ai-finance]
5) Real-World Examples of AI in Cybersecurity [https://www.group-ib.com/blog/examples-of-ai-in-cybersecurity/]
