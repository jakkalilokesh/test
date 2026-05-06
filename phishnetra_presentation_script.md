# PhishNetra — Live Presentation Script

> **Duration**: 20-25 minutes (adjustable)
> **Format**: Slide narration + Live Demo on localhost
> **Prerequisite**: Backend + Frontend + Docker containers running locally

---

## SLIDE 1 — Title Slide

### What to say:
> "Good morning/afternoon, respected panel members. I am [Name], and my team members are [Names]. Our final year project is **PhishNetra** — an enterprise-grade, AI-powered phishing email detection and analysis platform.
>
> In the next 20 minutes, we'll walk you through WHY we built this, HOW it works under the hood, and then give you a **live demonstration** of the system detecting a phishing email in real-time."

---

## SLIDE 2 — The Problem

### What to say:
> "Let's start with why this project matters.
>
> Every single day, **3.4 billion phishing emails** are sent worldwide. According to Verizon's 2024 Data Breach report, **91% of all cyberattacks** start with a phishing email. That's not a guess — that's an industry statistic.
>
> The challenge is that modern phishing attacks have evolved. Attackers now use **AI-generated text**, **Unicode obfuscation**, **homoglyph characters** — where they replace a Latin 'a' with a visually identical Cyrillic 'а' — and **zero-width invisible characters** to bypass traditional spam filters.
>
> So the question we set out to answer was: **Can we build a system that detects these advanced attacks using a multi-layered AI approach, and explain WHY an email is dangerous in plain English?**"

---

## SLIDE 3 — Our Solution (High-Level)

### What to say:
> "PhishNetra is our answer. It's not just another keyword scanner — it's a **9-layer deep analysis pipeline** that runs in parallel.
>
> When you upload an email, the system simultaneously runs:
> 1. **Rule-based pattern matching** — 80+ hand-crafted regex rules
> 2. **Machine Learning** — Random Forest + XGBoost ensemble
> 3. **NLP** — TF-IDF text classification
> 4. **Deep Learning** — BERT and SecBERT semantic analysis
> 5. **AI Intent Detection** — urgency, fear, and authority manipulation scoring
> 6. **Threat Intelligence** — checks URLs against VirusTotal, PhishTank, URLhaus
> 7. **URL Deep Analysis** — domain age, WHOIS, redirect chains, sandbox
> 8. **Attachment Scanning** — dangerous file types, macros, OCR
> 9. **Header Forensics** — SPF, DKIM, DMARC validation
>
> All 9 results are then fed into a **weighted risk scorer** that produces a final verdict from 0 to 100."

---

## SLIDE 4 — Tech Stack

### What to say:
> "For the tech stack:
> - **Backend**: FastAPI with Python, running asynchronous request handling. We use **Celery** with **Redis** as a task queue for heavy analysis jobs.
> - **Database**: PostgreSQL 16 for production, SQLite for development.
> - **ML Models**: scikit-learn for Random Forest, XGBoost for gradient boosting, HuggingFace Transformers for BERT.
> - **LLM Integration**: We support **6 LLM providers** — Groq, OpenAI, Anthropic Claude, HuggingFace, xAI Grok, and Ollama for fully offline operation. The system auto-falls to the next provider if one is down.
> - **Frontend**: React 18 with TypeScript, 26+ pages with code-splitting.
> - **Monitoring**: Full production stack — Prometheus metrics, Grafana dashboards, Loki log aggregation.
> - **Infrastructure**: Docker Compose for single-command deployment, Nginx reverse proxy, Terraform for cloud provisioning."

---

## SLIDE 5 — System Architecture Diagram

### What to say:
> "Here's the architecture diagram. Let me walk through the data flow:
>
> 1. The user uploads an email through the React frontend
> 2. The request hits our FastAPI backend through Nginx
> 3. FastAPI's `PhishingAnalyzer` orchestrator first runs **anti-evasion preprocessing** — this is Layer 0, it strips Unicode tricks, decodes HTML entities, normalizes homoglyphs, and deobfuscates leetspeak like `p@$$w0rd` back to `password`
> 4. Then all 9 analysis layers fire **in parallel** using Python's asyncio
> 5. Results aggregate into the Risk Scorer which applies **adaptive weighting** — if any layer is unavailable, its weight redistributes automatically
> 6. The final score, verdict, and AI explanation are persisted to PostgreSQL and returned to the frontend
> 7. Prometheus scrapes metrics, Grafana visualizes them, and Loki collects structured logs"

---

## SLIDE 6 — ML Pipeline Deep Dive

### What to say:
> "Let me explain the ML pipeline in detail.
>
> We extract **55+ numerical features** from each email across 4 categories:
> - **URL features**: count, average length, IP-based URLs, suspicious TLDs, shorteners
> - **Content features**: word count, urgency keyword density, fear keywords, caps ratio, HTML complexity score
> - **Header features**: SPF/DKIM/DMARC pass/fail, sender domain entropy, hop count
> - **Attachment features**: executable count, archive count, double extensions
>
> These features feed into our **ensemble model**:
> - **XGBoost** carries **50% weight** — it's our strongest classifier
> - **Random Forest** carries **35% weight** — it's interpretable and shows feature importance
> - **TF-IDF + Logistic Regression** carries **15% weight** — it catches text patterns the structured models miss
>
> The ensemble combines predictions using weighted averaging. Additionally, **BERT and SecBERT** run separately for deep semantic understanding — they can detect phishing intent even in grammatically correct, well-written emails."

---

## SLIDE 7 — Anti-Evasion (Innovation Highlight)

### What to say:
> "One of our key innovations is the **anti-evasion preprocessing module**. This is something most academic phishing detectors completely miss.
>
> Modern attackers use techniques like:
> - Inserting **zero-width Unicode characters** between letters: the word looks normal to humans but confuses NLP models
> - **Homoglyph attacks**: replacing Latin 'o' with Cyrillic 'о' — visually identical, different Unicode
> - **Leetspeak**: writing `@ccount` instead of `account`
> - **HTML comment stuffing**: splitting `login` as `lo<!--hidden-->gin` so keyword scanners miss it
>
> Our anti-evasion module runs **before** any analysis layer and strips all of these. We support 15 zero-width Unicode characters, 20+ Cyrillic homoglyphs, and full leetspeak deobfuscation. The evasion score itself is also fed into the risk calculator."

---

## 🖥️ LIVE DEMO — Switch to Browser

---

## DEMO STEP 1 — Login

### What to do:
1. Open `http://localhost:3000` in the browser
2. Login with your credentials

### What to say:
> "Let me now show you the system running live. This is our login page — we use **JWT-based authentication** with bcrypt password hashing. Access tokens expire in 30 minutes, and refresh tokens last 7 days."

---

## DEMO STEP 2 — Dashboard

### What to do:
1. After login, the Dashboard loads
2. Point out: Total analyses count, threat distribution chart, recent analyses table

### What to say:
> "This is the main dashboard. You can see:
> - Total emails analyzed to date
> - The **threat distribution** — how many were Safe, Low, Medium, High, or Critical
> - Recent analysis results with their verdicts
> - The system is fully responsive and supports dark mode — you can see the glassmorphism design throughout"

---

## DEMO STEP 3 — Email Analysis (Core Demo)

### What to do:
1. Navigate to `/analyze` (Email Analysis page)
2. Upload a prepared phishing `.eml` file OR paste a phishing email sample
3. Click "Analyze"
4. Wait for results (3-10 seconds)

### What to say while waiting:
> "I'm uploading a suspicious email. Right now, in the background:
> - The anti-evasion preprocessor is stripping any obfuscation
> - All 9 layers are running **simultaneously** — the rule engine, ML ensemble, BERT, TF-IDF, threat intelligence lookups, URL analysis, attachment scanning, and header forensics
> - The risk scorer is aggregating all results with adaptive weighting"

### What to say when results appear:
> "And here are the results. You can see:
> - The **overall risk score**: [X]/100 — classified as [verdict]
> - The **per-layer breakdown**: which layers flagged this email and why
> - The **triggered rules**: urgency keywords detected, brand impersonation found, suspicious URLs
> - The **ML confidence**: Random Forest says [X]%, XGBoost says [Y]%
> - The **AI explanation**: a human-readable summary explaining in plain English why this email is dangerous
> - The **top TF-IDF words**: the specific words that pushed the classifier toward 'phishing'
>
> This is what separates PhishNetra from simple spam filters — **full explainability**."

---

## DEMO STEP 4 — URL Scanner

### What to do:
1. Navigate to `/url-scanner`
2. Paste a suspicious URL (e.g., a known phishing URL or a test URL)
3. Click "Scan"

### What to say:
> "We also have a standalone URL scanner. I'll paste a suspicious URL here. The system checks it against **5 threat intelligence sources** in parallel — VirusTotal, PhishTank, URLhaus, AbuseIPDB, and our local phishing database sourced from GitHub community feeds."

---

## DEMO STEP 5 — Threat Intelligence

### What to do:
1. Navigate to `/threats`
2. Show the threat intel lookup interface

### What to say:
> "This is our Threat Intelligence page. You can look up any URL, domain, IP address, or file hash and get aggregated intelligence from multiple sources. Each source is weighted — VirusTotal at 30%, PhishTank at 20%, and so on. If multiple sources agree, the confidence score increases by 30%."

---

## DEMO STEP 6 — Analytics & History

### What to do:
1. Navigate to `/analytics` — show charts
2. Navigate to `/history` — show past analyses

### What to say:
> "The Analytics page shows detection trends over time, model performance metrics, and threat type distribution. The History page lets you browse all past analyses with search and filtering."

---

## DEMO STEP 7 — System Monitoring (if Docker stack is running)

### What to do:
1. Navigate to `/monitoring` or open Grafana at `http://localhost:3001`

### What to say:
> "Finally, our monitoring stack. We have **Prometheus** collecting metrics — request latency, analysis duration, ML model accuracy, error rates. **Grafana** visualizes these in real-time dashboards. And **Loki with Promtail** aggregates all structured logs for debugging."

---

## SLIDE 8 — Results & Accuracy

### What to say:
> "In terms of results:
> - Our ML ensemble achieves **99.16% accuracy** on our test dataset
> - The TF-IDF baseline alone achieves **95%+ accuracy**
> - The multi-layer approach gives us **near-zero false negatives** — we'd rather flag a legitimate email for review than miss a real phishing attack
> - Average analysis time is **3-8 seconds** for full 9-layer processing"

---

## SLIDE 9 — Future Scope

### What to say:
> "For future work, we envision:
> 1. **MTA Gateway Integration** — deploying as an inline mail filter (Postfix/Exchange plugin)
> 2. **Multilingual Support** — training BERT on non-English phishing datasets
> 3. **Federated Learning** — allowing organizations to improve the model without sharing email data
> 4. **Browser Extension** — real-time URL checking as users browse
> 5. **Mobile App** — on-device email scanning using TFLite models"

---

## SLIDE 10 — Q&A

### What to say:
> "That concludes our presentation and demonstration. We're happy to answer any questions."

---

## Frequently Asked Questions (Prepared Answers)

### Q: "Why not just use GPT-4 for everything?"
> "LLMs are powerful but have 3 problems for phishing detection: (1) they're slow — 2-5 seconds per call, (2) they cost money per token at scale, and (3) they hallucinate — they can confidently say an email is safe when it's not. Our approach uses LLMs only for **explanation**, not for detection. The actual detection is done by deterministic ML models and rules that are fast, free, and don't hallucinate."

### Q: "What happens if VirusTotal is down?"
> "The system uses **adaptive weighting**. If any layer is unavailable — whether it's an API timeout, model loading failure, or missing API key — its weight is automatically redistributed to the remaining layers. The system never crashes. It gracefully degrades."

### Q: "How is this different from Gmail's spam filter?"
> "Gmail's spam filter is a black box — you don't know why it flagged something. PhishNetra provides **full explainability**: which rules triggered, which ML features were important, which words the TF-IDF model flagged, and a natural-language AI explanation. We also provide **9 layers of analysis** vs. Gmail's single-layer approach."

### Q: "Can attackers bypass your system?"
> "No system is 100% foolproof, but PhishNetra makes it extremely difficult because an attacker would need to bypass **all 9 layers simultaneously**. Our anti-evasion module specifically targets the most common bypass techniques. And because we use BERT for semantic understanding, even completely reworded phishing attempts trigger the deep learning layer."

### Q: "Why did you choose FastAPI over Django/Flask?"
> "FastAPI gives us three things: (1) native async/await support — critical for running 9 analysis layers in parallel, (2) automatic OpenAPI documentation, and (3) Pydantic validation for all request/response models. Django is too heavyweight, and Flask doesn't have native async support."

### Q: "How do you handle model updates?"
> "Every trained model is saved with a **SHA256 integrity manifest**. When the system loads a model, it verifies the hash matches. If someone tampers with the model file, the system refuses to load it. We also keep timestamped version backups of every training run."

### Q: "What is the minimum hardware to run this?"
> "For development: 4GB RAM, any modern CPU, no GPU needed. For production: 8GB RAM recommended, and a GPU (even a cheap GTX 1050) speeds up BERT inference by 5-10x. The Docker Compose setup runs everything — backend, frontend, Redis, Prometheus, Grafana — on a single machine."
