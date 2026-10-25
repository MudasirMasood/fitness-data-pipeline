# 🏋️‍♂️ Fitness-Tech ELT Data Pipeline

> A production-grade Data Engineering pipeline built by a CS graduate and fitness professional, designed to ingest, structure, orchestrate, and load biometric and fitness user telemetry into an analytical data warehouse.

## 🚀 Project Overview
This project simulates an enterprise-level data pipeline architecture using a modern Medallion / ELT (Extract, Load, Transform) pattern:
1. **Extract:** Pulls raw data payloads from an upstream API source, handling network exceptions and storing immutable JSON extracts into a local data lake (`data/raw/`).
2. **Transform:** Normalizes, cleans, and flattens nested JSON payloads using Pandas into clean analytical datasets (`data/processed/`).
3. **Load:** Ingests the polished analytical data directly into a high-performance local columnar data warehouse (**DuckDB**).
4. **Orchestrate:** Automates the entire end-to-end execution flow via a master orchestration script with logging and error handling.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Core Libraries:** Requests, Pandas, DuckDB, Dotenv, Logging, Glob
* **Architecture Pattern:** Extract, Load, Transform (ELT) / Local Data Lake & Warehouse / Pipeline Orchestration
* **Version Control:** Git & GitHub

## 📂 Project Structure
```text
fitness-data-pipeline/
│
├── data/                  # Local Data Lake & Warehouse (Ignored by Git)
│   ├── raw/               # Immutable raw JSON extractions
│   ├── processed/         # Cleaned analytical CSV outputs
│   └── warehouse.duckdb   # DuckDB analytical data warehouse file
├── scripts/               # Core Python automation modules
│   ├── extract.py         # API Ingestion module
│   ├── transform.py       # Data cleaning & flattening module
│   ├── load.py            # Warehouse loading module (DuckDB)
│   └── run_pipeline.py    # Master end-to-end ELT orchestrator
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

Run the Full Automated ELT Pipeline:
python scripts/run_pipeline.py

Query the DuckDB Data Warehouse:
You can inspect your loaded tables directly via the terminal using Python:
python -c "import duckdb; conn = duckdb.connect('data/warehouse.duckdb'); print(conn.execute('SELECT * FROM fact_fitness_users').fetchdf()); conn.close()"

