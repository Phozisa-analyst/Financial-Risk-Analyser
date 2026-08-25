# Custom Credit Risk & Financial Health Analyzer

⚠️ **Status: Active Development (MVP scheduled for completion: September 2026)**

## 📌 Project Overview
This repository contains a full-stack data pipeline and automated decision-engine prototype designed for retail banking institutions. The application simulates how financial analysts evaluate customer creditworthiness, monitor debt-to-income (DTI) metrics, and run automated risk classification logic based on structured business rules.

Built specifically to demonstrate cross-functional capability between **Bespoke Software Development** and **Technical Business Analysis**.

---

## 🛠️ Architecture & Tech Stack
- **Language:** Python 3.11+
- **Data Engineering:** Pandas & NumPy (Data cleansing, validation, and pipeline transformations)
- **Database Layer:** SQLite3 (Relational data modeling, foreign key indexing, and custom aggregation queries)
- **Presentation Layer:** Streamlit (Rapid prototyping framework for interactive, data-driven web interfaces)

---

## 💡 Core Business Logic & Acceptance Criteria
This project embeds strict regulatory and financial criteria into its data layer using Behavior-Driven Development (BDD) frameworks:

### Scenario 1: Automated Loan Pre-Approval
* **Given** a retail banking customer submits a loan application
* **When** their calculated Credit Score is `>= 650`
* **And** their Debt-to-Income (DTI) ratio is `< 40%`
* **Then** flag the application status automatically as `Pre-Approved`

### Scenario 2: High-Risk Account Mitigation
* **Given** a customer profile is evaluated by the engine
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
   pip install pandas streamlit
   ```
3. Run the data pipeline to initialize the database:
   ```bash
   python data_pipeline.py
   ```
4. Launch the interface:
   ```bash
   streamlit run app.py
   ```
