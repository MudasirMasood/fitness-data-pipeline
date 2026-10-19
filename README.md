# 🏋️‍♂️ Fitness-Tech ELT Data Pipeline

> A production-grade Data Engineering pipeline built by a CS graduate and fitness professional, designed to ingest, structure, and orchestrate biometric and fitness user telemetry.

## 🚀 Project Overview
This project simulates an enterprise-level data pipeline architecture using a modular design pattern. It extracts raw data payloads from an upstream API source, handles network exceptions and logging securely, drops raw extracts into a localized data lake structure (`data/raw/`), transforms them via Pandas into analytical datasets (`data/processed/`), and automates the entire flow through a master orchestration script.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Libraries:** Requests, Pandas, Dotenv, Logging, Glob
* **Architecture Pattern:** Extract, Load, Transform (ELT) / Data Lake Zone Structure / Pipeline Orchestration
* **Version Control:** Git & GitHub

## 📂 Project Structure
```text
fitness-data-pipeline/
│
├── data/                  # Local Data Lake storage (Ignored by Git)
│   ├── raw/               # Immutable raw JSON extractions
│   └── processed/         # Cleaned analytical CSV outputs
├── scripts/               # Core Python automation modules
│   ├── extract.py         # Ingestion and API extraction module
│   ├── transform.py       # Data cleaning and modeling module
│   └── run_pipeline.py    # Master orchestration & execution script
├── .gitignore             # Excludes sensitive and temporary files
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation

⚙️ Getting Started & Execution

Clone the repository:

git clone [https://github.com/MudasirMasood/fitness-data-pipeline.git](https://github.com/MudasirMasood/fitness-data-pipeline.git)
cd fitness-data-pipeline

Set up a Virtual Environment:

python -m venv venv
venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Run the Automated Master Pipeline:
python scripts/run_pipeline.py