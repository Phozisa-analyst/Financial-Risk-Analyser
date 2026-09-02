# Custom Credit Risk & Financial Health Analyzer (ERP Integration Prototype)

⚠️ **Status: Active Development (MVP Version 1.0 Live | Next Sprint: Advanced Analytics Integration)**

## 📌 Project Overview
This repository contains a full-stack data pipeline and automated decision-engine prototype designed for retail banking environments. The application simulates how data from enterprise ERP architectures (such as **SAP S/4HANA Private Cloud**) is extracted, cleaned, and transformed into structured analytical databases to run automated credit risk and portfolio evaluation engines.

Built specifically to demonstrate cross-functional capability between **Bespoke Software Development** and **Technical Business Analysis**.

---

## 🛠️ Architecture & Core System Layout
- **Language:** Python 3.11+
- **Data Pipeline:** Pandas & NumPy (Emulating an ETL layer extracting from source systems, executing data deduplication, and fixing missing ledger flags)
- **Database Layer:** SQLite3 (Relational data modeling mimicking normalized target warehouses, structured with primary/foreign key indexing)
- **Presentation Layer:** Streamlit (Rapid prototyping framework for interactive, stakeholder-facing analytical dashboards)

---

## 💡 Core Business Logic & Acceptance Criteria
This project embeds strict regulatory, compliance, and cost allocation logic into its data layer using Behavior-Driven Development (BDD) frameworks to maintain strict ISTQB auditing standards:

### Scenario 1: Automated Loan Pre-Approval
* **Given** an enterprise customer profile is loaded from the data layer
* **When** their calculated Credit Score is `>= 650`
* **And** their Debt-to-Income (DTI) ratio is `< 40%`
* **Then** flag the application status automatically as `Pre-Approved`

### Scenario 2: High-Risk Account Mitigation
* **Given** a customer ledger profile is evaluated by the engine
* **When** their credit score drops below `580` **OR** their DTI exceeds `45%`
* **Then** append a `High Risk` flag and route the profile to the manual review queue

---

## 📂 Repository Structure
```text
├── data_pipeline.py  # Script for messy synthetic data generation, cleaning, and SQLite injection
├── app.py            # Streamlit dashboard frontend and visual analytics engine
├── README.md         # Technical architecture documentation
└── banking.db        # Local relational database file (Generated at runtime)
```

---

## 🚀 How to Run the App Locally
1. Clone this repository:
   ```bash
   git clone https://github.com
   ```
2. Install dependencies:
   ```bash
   python -m pip install pandas numpy streamlit
   ```
3. Run the data pipeline to initialize the database:
   ```bash
   python data_pipeline.py
   ```
4. Launch the interface:
   ```bash
   streamlit run app.py
   ```
