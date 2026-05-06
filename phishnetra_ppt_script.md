# PhishNetra PPT — Slide-by-Slide Presentation Script

> **Total Slides**: 13 | **Estimated Duration**: 20–25 minutes
> **PPT File**: `PhishNetra A Multi-Layer Intelligent Email Phishing Detection System.pptx`

---

## SLIDE 1 — Title Slide
**Slide Content**: RUCE Kurnool branding, Project title, Guide name, Team members

### 🎤 What to Say:

> "Good morning/afternoon respected chairperson, panel members, and our project guide **V. Sathish Kumar sir**.
>
> We are from the **Department of Computer Science and Engineering, Rayalaseema University College of Engineering, Kurnool**.
>
> Our team members are:
> - Jakkali Lokesh (23RU5A0503)
> - Dasari Abhilash (23RU5A0501)
> - Mangali Mahalakshmi (22RU1A0533)
> - Gajula Ansar Basha (23RU5A0502)
> - Kuruva Krishnaveni (22RU1A0529)
>
> Our project title is **'PhishNetra — A Multi-Layer Intelligent Email Phishing Detection System.'**
>
> The name 'PhishNetra' comes from combining 'Phish' — referring to phishing attacks — and 'Netra', which means 'eye' in Sanskrit. So PhishNetra literally means **the eye that watches for phishing**."

**⏱ Duration**: ~1 minute

---

## SLIDE 2 — Introduction / Overview
**Slide Content**: Key points about the project + 99.16% accuracy highlight

### 🎤 What to Say:

> "Let us begin with why we chose this project.
>
> Phishing is one of the **most dangerous and rapidly evolving cybersecurity threats** in the world today. According to the Verizon 2024 Data Breach Investigations Report, **91% of all cyberattacks begin with a phishing email**. That means nearly every major data breach, ransomware incident, or credential theft starts with someone clicking a malicious link in an email.
>
> Now, the problem with **traditional email security systems** — like basic spam filters — is that they rely on **static rules and known signatures**. If an attacker slightly modifies the wording, uses Unicode tricks, or disguises a URL, these systems completely fail.
>
> This motivated us to build a system that doesn't rely on any single detection technique. Instead, PhishNetra uses a **multi-layer approach** — combining Machine Learning, Natural Language Processing, Threat Intelligence feeds, and rule-based heuristics — all running **in parallel**.
>
> And the result speaks for itself — our system achieved an overall classification accuracy of **99.16%** on our test dataset.
>
> The core innovation here is that we are not just detecting phishing — we are **explaining WHY** an email is suspicious, in plain English, so that even a non-technical user can understand the threat."

**⏱ Duration**: ~2 minutes

---

## SLIDE 3 — Problem Statement
**Slide Content**: 5 limitations of existing systems

### 🎤 What to Say:

> "Now let's look at the **specific problems** with current phishing detection systems. We identified five major limitations:
>
> **First — Static Rule-Based Detection.** Traditional systems use fixed rules like 'block emails containing the word lottery'. But attackers easily bypass these by using synonyms, leetspeak like writing 'l0ttery' with a zero, or embedding words inside HTML comments.
>
> **Second — Signature-Based Dependency.** These systems maintain a database of known malicious URLs, email addresses, and file hashes. The problem? They can only detect **known threats**. A brand-new phishing URL that was created 5 minutes ago? It passes right through.
>
> **Third — No Zero-Day Detection.** This is the critical gap. Existing systems have **zero capability** to detect a phishing attack that has never been seen before. They cannot understand the *intent* of an email — only match patterns.
>
> **Fourth — High False Positives.** Single-layer systems frequently misclassify legitimate emails as threats. For example, a genuine email from your bank saying 'please verify your account' gets flagged as phishing because it contains trigger keywords. This erodes user trust.
>
> **Fifth — Limited Analysis Capability.** Most existing systems analyze only one dimension — either the URL, or the text, or the header. They never look at **all of these together**. A sophisticated attack might have a clean URL, clean header, but highly manipulative text — and a single-layer system would miss it entirely.
>
> Our project addresses **all five of these limitations** simultaneously."

**⏱ Duration**: ~2.5 minutes

---

## SLIDE 4 — Proposed Solution
**Slide Content**: 5 advantages of PhishNetra's approach

### 🎤 What to Say:

> "Here is our proposed solution and the key advantages it provides:
>
> **Multi-Layer Detection** — Instead of a single analysis engine, PhishNetra runs **9 independent detection layers in parallel**. These include a Rule Engine with 80+ patterns, a Machine Learning ensemble (Random Forest + XGBoost), TF-IDF text classification, BERT deep learning, AI-powered intent detection, Threat Intelligence lookups across VirusTotal, PhishTank, URLhaus, and AbuseIPDB, URL deep analysis with domain WHOIS and redirect chain tracing, attachment scanning with OCR, and full email header forensics including SPF, DKIM, and DMARC validation. Each layer produces its own risk score, and all 9 scores are aggregated by our weighted risk scorer.
>
> **ML + NLP + Threat Intelligence** — This is the hybrid approach. Machine Learning handles **structured features** — like URL length, number of suspicious keywords, sender domain entropy. NLP handles **unstructured text** — understanding the actual meaning and intent of the email using BERT transformers. And Threat Intelligence provides **real-time external reputation data** from community databases.
>
> **Hybrid Detection Model** — By combining structured feature analysis and semantic text understanding, we catch attacks that either approach alone would miss. For example, an email with perfect grammar and clean URLs but using psychological manipulation (urgency, fear) — our BERT and intent detection layers catch this.
>
> **Real-Time Analysis** — Our backend uses **FastAPI** with Python's asyncio, running all 9 layers concurrently. Full analysis completes in **3 to 8 seconds** for a typical email.
>
> **Improved Accuracy & Reliability** — The multi-layer consensus approach means false positives drop dramatically. An email is flagged as phishing only when **multiple independent layers agree**, not based on a single keyword match."

**⏱ Duration**: ~3 minutes

---

## SLIDE 5 — System Architecture
**Slide Content**: Input → Processing → Analysis → Decision pipeline

### 🎤 What to Say:

> "This slide shows the **high-level system architecture** of PhishNetra. Let me walk through the data flow step by step:
>
> **Input Stage** — The user uploads a raw email file, either `.eml` or `.msg` format, or pastes email content directly through our React web interface. The request is sent via REST API to our FastAPI backend. We also support direct IMAP integration — you can connect your Gmail or Outlook account and PhishNetra will automatically scan incoming emails.
>
> **Processing Stage** — This is where our **anti-evasion preprocessing** runs. Before any analysis happens, we strip 8 types of attacker obfuscation:
> - Zero-width invisible Unicode characters — 15 different types
> - Cyrillic homoglyphs — characters that look identical to Latin letters
> - HTML comment stuffing — where attackers split keywords like `lo<!--hidden-->gin`
> - Leetspeak — converting `p@$$w0rd` back to `password`
> - Base64 encoded suspicious content
> - HTML entity encoding
> - Unicode NFKC normalization
> - Invisible CSS text hiding
>
> This preprocessing is critical because without it, our NLP and rule engine would miss obfuscated phishing keywords.
>
> **Analysis Stage** — All 9 detection layers fire **simultaneously** using Python's asyncio.gather(). This parallel execution is why we achieve 3-8 second response times instead of 30+ seconds if run sequentially.
>
> **Decision Stage** — Our Risk Scorer aggregates all 9 layer outputs using **adaptive weighted scoring**. The key innovation here is: if any layer is unavailable — say VirusTotal's API is down — the system doesn't crash. It automatically **redistributes that layer's weight** to the remaining layers. The final output is a risk score from 0 to 100, classified as Safe, Low, Medium, High, or Critical."

**⏱ Duration**: ~3 minutes

---

## SLIDE 6 — System Design (Layers)
**Slide Content**: 5 system layers — Input, Processing, Analysis, Threat Intel, Decision

### 🎤 What to Say:

> "Let me explain each system layer in more detail:
>
> **Layer 5 — Input Layer.** This handles email ingestion. Python's `email.parser` module extracts the raw headers, plain-text body, HTML body, and all attachments. Each attachment gets a SHA256 hash computed for threat intelligence lookups.
>
> **Layer 4 — Processing Layer.** This is our **feature extraction** stage. We extract **55+ numerical features** from every email — URL statistics like count, average length, suspicious TLDs; content statistics like word count, urgency keyword density, caps ratio; header features like SPF/DKIM pass/fail, hop count, sender domain entropy; and attachment features like executable count and double extensions. These features become the input vector for our ML models.
>
> **Layer 3 — Analysis Layer.** This is the core — where all 9 detection engines run. The ML ensemble (Random Forest at 35% weight + XGBoost at 50% weight) operates on the structured feature vector. The TF-IDF + Logistic Regression model operates on the raw email text using word-level and character-level n-grams. BERT and SecBERT provide deep semantic understanding. The Rule Engine matches 80+ regex patterns. URL analysis checks domain reputation. Attachment scanning uses OCR to extract text from images.
>
> **Layer 2 — Threat Intelligence Layer.** We query 5 external sources in parallel — VirusTotal, PhishTank, URLhaus, AbuseIPDB, and our local phishing database sourced from GitHub community feeds. Each source has a weighted contribution to the final score.
>
> **Layer 1 — Decision & Presentation Layer.** The Risk Scorer computes the final weighted score. Then our AI Explainer module generates a human-readable explanation — optionally enhanced by an LLM like Groq's Llama 3.3 70B — explaining exactly which indicators were found and what the user should do."

**⏱ Duration**: ~2.5 minutes

---

## SLIDE 7 — Detection Workflow
**Slide Content**: 5-step workflow — Parse → Extract → Analyze → Validate → Score

### 🎤 What to Say:

> "This slide shows the detection workflow in sequential order:
>
> **Step 1 — Email Parse.** The raw email bytes are parsed to extract headers, body (both text and HTML), attachments, and all embedded URLs. The parser handles MIME multipart emails, base64-encoded bodies, and nested attachments.
>
> **Step 2 — Feature Extract.** After parsing, the anti-evasion preprocessor runs first to clean the text. Then 55+ features are extracted across 4 categories: URL, content, header, and attachment features. The cleaned text is also tokenized for the TF-IDF and BERT models.
>
> **Step 3 — Parallel Analysis.** All 9 detection modules execute concurrently. This is the most compute-intensive stage. Each module produces its own independent score and a list of detection indicators.
>
> **Step 4 — Threat Validate.** URLs are cross-referenced against 5 threat intelligence sources. If multiple sources independently flag the same URL, the confidence score increases by 30%. This multi-source agreement mechanism significantly reduces false positives.
>
> **Step 5 — Risk Score.** The weighted aggregation engine collects all 9 layer outputs and computes the final score using adaptive weighting. The system then classifies the email: 0-20 = Safe, 20-40 = Low Risk, 40-60 = Medium, 60-80 = High, 80-100 = Critical. The result, along with all per-layer details and the AI explanation, is persisted to PostgreSQL and returned to the user."

**⏱ Duration**: ~2 minutes

---

## SLIDE 8 — Module Structure
**Slide Content**: 8 modules listed

### 🎤 What to Say:

> "Here's the breakdown of every module in the system:
>
> **Email Parser** — Handles `.eml` and `.msg` formats, extracts all email components.
>
> **ML Engine** — This is actually an **ensemble of three models**: Random Forest (100 trees, max depth 15), XGBoost (100 estimators, learning rate 0.1), and TF-IDF + Logistic Regression. XGBoost carries the highest weight at 50%. The ensemble uses weighted probability averaging — if any model is unavailable, weights auto-normalize.
>
> **NLP Analyzer** — Uses **DistilBERT** for general semantic understanding and **SecBERT** — a cybersecurity-domain-specific BERT model pre-trained on security text — for specialized phishing intent detection. Both models tokenize up to 512 tokens and produce binary classification probabilities.
>
> **URL Analysis** — Extracts all URLs from both text and HTML body. For each URL: checks domain WHOIS age, traces redirect chains, validates SSL certificates, detects typosquatting, IP-based URLs, suspicious TLDs (.xyz, .top, .click), and URL shorteners.
>
> **Threat Intelligence** — Aggregates data from VirusTotal (30% weight), PhishTank (20%), URLhaus (20%), Local Phishing DB (20%), and AbuseIPDB (10%). All queries run in parallel with a 30-second timeout and circuit breaker pattern for resilience.
>
> **Attachment Analysis** — Scans for dangerous extensions (.exe, .scr, .bat, .ps1), double extensions (invoice.pdf.exe), macro-enabled documents, and uses **OCR** to extract text from image attachments and run it through the rule engine.
>
> **Decision Engine** — The `RiskScorer` module with 8 weighted inputs and adaptive redistribution. Also includes override mechanisms — for example, if VirusTotal confirms malware, it immediately escalates to Critical regardless of other scores.
>
> **User Interface** — React 18 frontend with **26+ pages** including real-time analysis, threat map, forensics lab, URL sandbox, campaign tracker, analytics dashboards, and system monitoring."

**⏱ Duration**: ~3 minutes

---

## SLIDE 9 — Core Models (ML & NLP)
**Slide Content**: Random Forest, BERT, Feature-Based, Hybrid approach

### 🎤 What to Say:

> "Let me go deeper into the core ML and NLP models:
>
> **Random Forest Classifier** — This is our interpretable baseline. It operates on the 55-dimensional structured feature vector. The key advantage of Random Forest is **explainability** — we can extract the top 10 most important features for each prediction and show the user exactly WHICH features drove the classification. For example: 'This email was flagged because sender_domain_entropy is 4.2 (very high — suggests randomly generated domain), urgency_keyword_count is 5, and spf_fail is 1.'
>
> **BERT Language Model** — We use two BERT variants. **DistilBERT** (distilbert-base-uncased) provides general-purpose semantic understanding — it understands context, sarcasm, and implicit threats. **SecBERT** (jackaduma/SecBERT) is specifically pre-trained on cybersecurity text — it's been fine-tuned to recognize security-specific language patterns. Together, they catch **zero-day phishing** — emails that have never been seen before but use psychological manipulation.
>
> **Feature-Based Analysis** — This is the TF-IDF component. We use both **word-level TF-IDF** (up to 10,000 features, unigrams + bigrams + trigrams) and **character-level TF-IDF** (2,500 features, 3-5 character grams). The character-level component is specifically designed to catch **obfuscated text** and leetspeak that word-level analysis misses. The combined sparse feature matrix feeds into Logistic Regression with balanced class weights.
>
> **Hybrid Model Approach** — The final innovation. Instead of trusting any single model, we compute a **weighted ensemble probability**:
>
> `Final Score = (RF × 0.35) + (XGBoost × 0.50) + (TF-IDF × 0.15)`
>
> This hybrid approach is why we achieve **99.16% accuracy** — it's significantly higher than any individual model alone."

**⏱ Duration**: ~2.5 minutes

---

## SLIDE 10 — Technology Stack & Implementation
**Slide Content**: Frontend/Backend, ML/NLP, Data Layer, Deployment

### 🎤 What to Say:

> "For the implementation, we chose a modern, production-grade technology stack:
>
> **Frontend** — React 18 with TypeScript for type safety, Vite for fast builds, and Zustand for lightweight state management. We implemented **26+ pages** with lazy loading for code-splitting, a Command Palette (Ctrl+K) for power users, a built-in Security Chatbot, and a Guided Tour for onboarding. The design uses glassmorphism aesthetics with full dark and light mode support.
>
> **Backend** — FastAPI with Python 3.11+. FastAPI was chosen over Django and Flask for three specific reasons: native async/await support for running 9 layers in parallel, automatic OpenAPI documentation, and Pydantic model validation. We also use **Celery with Redis** as a distributed task queue for offloading heavy ML analysis to background workers.
>
> **ML/NLP Stack** — scikit-learn for Random Forest and TF-IDF, XGBoost for gradient boosting, HuggingFace Transformers for BERT/DistilBERT/SecBERT, and SHAP for model explainability. We also integrate **6 LLM providers** — Groq, OpenAI, Anthropic Claude, HuggingFace Inference, xAI Grok, and Ollama for fully offline LLM support. The system auto-falls to the next provider if one is unavailable.
>
> **Data Layer** — PostgreSQL 16 for production with asyncpg driver for async database operations. Redis serves triple duty: Celery broker, response cache, and pub/sub event bus.
>
> **Deployment** — Docker and Docker Compose for single-command deployment. We also include Terraform scripts for cloud provisioning and a full **monitoring stack**: Prometheus for metrics, Grafana for dashboards, Loki and Promtail for log aggregation, and OpenTelemetry for distributed tracing.
>
> The complete setup process is: `git clone → docker-compose up` — and the entire platform is running."

**⏱ Duration**: ~2.5 minutes

---

## SLIDE 11 — Results
**Slide Content**: Results screenshots / metrics

### 🎤 What to Say:

> "Now let's look at the results.
>
> *(If showing live demo, switch to browser here)*
>
> Let me demonstrate the system working on a real phishing email sample.
>
> *(Upload a prepared phishing .eml file or paste phishing email text)*
>
> As you can see, the system has classified this email as **[High/Critical]** with a risk score of **[X]/100**.
>
> Looking at the per-layer breakdown:
> - The **Rule Engine** detected [X] suspicious patterns — urgency keywords, credential harvesting phrases
> - The **ML Ensemble** gave a phishing probability of [X]% — XGBoost was the strongest signal
> - **BERT** flagged social engineering intent with [X]% confidence
> - **TF-IDF** identified the top contributing words — you can see 'verify', 'account', 'immediately' have the highest positive coefficients pushing toward phishing
> - **Threat Intelligence** checked [X] URLs against 5 databases — [results]
>
> And here is the **AI-generated explanation** in plain English, telling the user exactly why this email is dangerous and what they should do.
>
> This level of explainability is what separates PhishNetra from black-box solutions — every verdict is transparent and auditable."

**⏱ Duration**: ~3 minutes (varies with live demo)

---

## SLIDE 12 — Conclusion & Future Scope
**Slide Content**: 99.16% accuracy, 97%+ precision, ~1% FP, future plans

### 🎤 What to Say:

> "To conclude, our system demonstrates **strong real-world performance**:
>
> - **99.16% overall accuracy** on our benchmark test dataset
> - **97%+ precision** in phishing identification — meaning when PhishNetra says an email is phishing, it is correct 97% of the time
> - **Less than 1% false positive rate** — legitimate emails are very rarely misclassified as threats
>
> Our key findings are:
> 1. The **multi-layer approach outperforms single-model baselines** — our ensemble beats standalone Random Forest by 4% and standalone TF-IDF by 6% in accuracy
> 2. The **hybrid ML + NLP approach** catches attack types that either approach alone would miss — ML catches structural anomalies while BERT catches semantic manipulation
> 3. The **modular architecture** is designed for future expansion — new detection modules can be plugged in without modifying existing code
>
> For **future scope**, we have identified several enhancement paths:
> 1. **Real-time email gateway integration** — deploying PhishNetra as an inline mail filter (Postfix/Exchange plugin) for real-time protection
> 2. **Adversarial training** — training our models against adversarial phishing samples to improve robustness against attacker adaptation
> 3. **Expanded threat feeds** — integrating more threat intelligence sources like Google Safe Browsing and emerging community databases
> 4. **Multilingual support** — extending BERT models to detect phishing in non-English languages
> 5. **Federated learning** — allowing organizations to improve the shared model without sharing sensitive email data
> 6. **Browser extension** — a Chrome/Firefox plugin for real-time URL checking while browsing"

**⏱ Duration**: ~2 minutes

---

## SLIDE 13 — Thank You & Q&A
**Slide Content**: Team names, Q&A

### 🎤 What to Say:

> "That concludes our presentation on PhishNetra. We would like to thank our guide **V. Sathish Kumar sir** for his continuous support and guidance throughout this project.
>
> We are now open for any questions. Thank you."

**⏱ Duration**: ~30 seconds

---

---

# 📋 Prepared Q&A — Detailed Answers

## Q1: "Why 9 layers? Isn't that overkill?"
> "No, sir/ma'am. The reason is **defense-in-depth** — the same principle used in military security. No single detection technique is perfect. Rule engines miss zero-day attacks. ML models can be fooled by adversarial inputs. Threat intelligence databases have delayed updates. By running 9 independent layers and requiring consensus, we make it extremely difficult for an attacker to bypass ALL layers simultaneously. Each layer covers the blind spots of the others."

## Q2: "What is the difference between your system and Gmail's spam filter?"
> "Three key differences: (1) Gmail's filter is a **black box** — you never know why an email was flagged. PhishNetra provides **full explainability** with per-layer breakdown and AI-generated explanations. (2) Gmail uses a **single detection model** internally. We use 9 independent models in parallel. (3) Gmail doesn't expose threat intelligence data. PhishNetra shows you exactly which VirusTotal engines flagged a URL, the PhishTank verification status, and the AbuseIPDB confidence score."

## Q3: "How do you handle false positives?"
> "Our multi-layer consensus approach inherently reduces false positives. A legitimate email from your bank saying 'verify your account' might trigger the Rule Engine, but it will NOT trigger BERT (which understands the context is genuine), will NOT trigger Threat Intel (the bank's URL is clean), and will NOT trigger header forensics (SPF/DKIM will pass). Since the majority of layers give a safe verdict, the final weighted score stays low. Only emails that are flagged by **multiple independent layers** get classified as phishing."

## Q4: "What is BERT and why did you use it?"
> "BERT stands for Bidirectional Encoder Representations from Transformers. It's a deep learning model developed by Google that understands language **contextually** — it reads both left and right context of every word simultaneously. We use it because traditional keyword matching can't understand intent. For example, 'Your account will be suspended unless you verify immediately' — a keyword scanner sees 'account', 'suspended', 'verify' as individual words. BERT understands the full sentence means the email is trying to **create urgency and fear** to trick you into clicking a link. We specifically use two variants: DistilBERT for general understanding and SecBERT which is pre-trained on cybersecurity text."

## Q5: "What is TF-IDF?"
> "TF-IDF stands for Term Frequency-Inverse Document Frequency. It converts text into numerical vectors based on how important each word is. 'Term Frequency' measures how often a word appears in the email. 'Inverse Document Frequency' measures how rare that word is across all emails in our training set. Words that appear frequently in phishing emails but rarely in legitimate emails get high TF-IDF scores. For example, 'verify' has a high TF-IDF score in phishing context. We use both word-level n-grams (1-3 words) and character-level n-grams (3-5 characters) to catch both normal words and obfuscated text like 'p@$$word'."

## Q6: "What happens if the internet is down?"
> "The system is designed for **graceful degradation**. If the internet is down, the Threat Intelligence layer (VirusTotal, PhishTank, etc.) becomes unavailable. But the system doesn't crash — the Risk Scorer uses **adaptive weighting** to redistribute that layer's weight to the remaining layers (Rule Engine, ML, BERT, TF-IDF). These models all run locally and don't need internet. We also support **Ollama** — a local LLM that runs completely offline — for AI explanations. So even with zero internet, the system provides a complete analysis using 7 out of 9 layers."

## Q7: "How did you achieve 99.16% accuracy?"
> "Three factors contributed: (1) **Ensemble learning** — combining Random Forest, XGBoost, and TF-IDF is statistically stronger than any individual model. (2) **Feature engineering** — we extract 55+ features that capture URL patterns, email structure, linguistic cues, and authentication signals. (3) **BERT semantic understanding** — catches phishing that structured features miss. The 99.16% is measured on our test dataset using stratified train/test split with cross-validation."

## Q8: "What is anti-evasion and why is it important?"
> "Anti-evasion is our preprocessing module that runs BEFORE any analysis. Modern phishers use tricks to bypass detection: they insert invisible Unicode characters between letters so 'password' looks normal to humans but the scanner sees 'p\u200Ba\u200Bssword'. They use Cyrillic characters that look identical to Latin — the letter 'a' in Cyrillic has a different Unicode codepoint than Latin 'a'. They write 'p@$$w0rd' using leetspeak. Our anti-evasion module strips ALL of these tricks, converting the text back to its clean form before the rule engine and ML models process it. Without this module, our detection rate drops by approximately 8-12% on obfuscated phishing samples."

## Q9: "Can you explain the Risk Scorer's adaptive weighting?"
> "Each of our 9 layers has a default weight — Rule Engine 20%, ML Ensemble 20%, BERT 15%, AI Enhancements 10%, Threat Intel 15%, URL Analysis 10%, Attachments 5%, Headers 5%. If any layer is unavailable — say the ML models aren't loaded — its 20% weight doesn't become zero. Instead, it's **redistributed proportionally** to the remaining layers. So if ML is down, Rule Engine might go from 20% to 25%, BERT from 15% to 19%, and so on. The weights always sum to 100%. This means the system maintains reliable scoring even when operating in degraded mode."

## Q10: "What is your deployment architecture?"
> "We use **Docker Compose** for single-command deployment. The stack includes: FastAPI backend container, React frontend served via Nginx, PostgreSQL database, Redis (for Celery task queue and caching), Prometheus for metrics collection, Grafana for visualization dashboards, and Loki+Promtail for centralized log aggregation. All of these start with one command: `docker-compose up`. For cloud deployment, we have Terraform scripts that can provision the infrastructure on any cloud provider."
