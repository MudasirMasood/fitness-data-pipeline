import os
import glob
import logging
import duckdb
import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [LOADER] %(message)s",
    handlers=[logging.StreamHandler()]
)

class FitnessDataDataLoader:
    def __init__(self, db_path="data/warehouse.duckdb"):
        self.db_path = db_path
        os.makedirs("data", exist_ok=True)

    def get_latest_processed_file(self):
        list_of_files = glob.glob('data/processed/*.csv')
        if not list_of_files:
            raise FileNotFoundError("No processed CSV files found to load!")
        latest_file = max(list_of_files, key=os.path.getctime)
        logging.info(f"Found latest processed file for loading: {latest_file}")
        return latest_file

    def load_data_to_duckdb(self, csv_file_path):
        logging.info("Starting data load into DuckDB warehouse...")
        
        # Read processed CSV into Pandas DataFrame
        df = pd.read_csv(csv_file_path)

        # Connect to DuckDB database file (creates it automatically if it doesn't exist)
        conn = duckdb.connect(database=self.db_path, read_only=False)

        # Load DataFrame into a table named 'fact_fitness_users'
        conn.execute("CREATE TABLE IF NOT EXISTS fact_fitness_users AS SELECT * FROM df WHERE 1=0;")
        conn.execute("INSERT INTO fact_fitness_users SELECT * FROM df;")

        # Verify row count inside the database
        result = conn.execute("SELECT COUNT(*) FROM fact_fitness_users;").fetchone()
        logging.info(f"Successfully loaded data into DuckDB table 'fact_fitness_users'. Total rows in table: {result[0]}")

        conn.close()
        logging.info("Database connection closed securely.")

if __name__ == "__main__":
    loader = FitnessDataDataLoader()
    latest_csv = loader.get_latest_processed_file()
    loader.load_data_to_duckdb(latest_csv)