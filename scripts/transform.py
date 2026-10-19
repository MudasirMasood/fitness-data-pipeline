import os
import glob
import logging
import pandas as pd
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

class FitnessDataTransformer:
    def __init__(self):
        self.raw_dir = "data/raw"
        self.processed_dir = "data/processed"
        os.makedirs(self.processed_dir, exist_ok=True)

    def get_latest_raw_file(self) -> str:
        list_of_files = glob.glob(os.path.join(self.raw_dir, "*.json"))
        if not list_of_files:
            raise FileNotFoundError(f"No raw JSON files found in {self.raw_dir}. Run extract.py first!")
        latest_file = max(list_of_files, key=os.path.getctime)
        logging.info(f"Found latest raw file: {latest_file}")
        return latest_file

    def transform_data(self, file_path: str) -> pd.DataFrame:
        logging.info("Starting data transformation process...")
        df = pd.read_json(file_path)

        if 'address' in df.columns:
            df['city'] = df['address'].apply(lambda x: x.get('city') if isinstance(x, dict) else None)
            df['zipcode'] = df['address'].apply(lambda x: x.get('zipcode') if isinstance(x, dict) else None)

        if 'company' in df.columns:
            df['company_name'] = df['company'].apply(lambda x: x.get('name') if isinstance(x, dict) else None)

        columns_to_keep = ['id', 'name', 'username', 'email', 'city', 'zipcode', 'company_name']
        existing_cols = [col for col in columns_to_keep if col in df.columns]
        df_transformed = df[existing_cols].copy()

        df_transformed['name'] = df_transformed['name'].str.title()
        df_transformed['email'] = df_transformed['email'].str.lower()
        df_transformed.dropna(subset=['email'], inplace=True)
        df_transformed['processed_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        logging.info(f"Transformation complete. Cleaned records count: {len(df_transformed)}")
        return df_transformed

    def save_processed_data(self, df: pd.DataFrame) -> str:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"processed_fitness_metrics_{timestamp}.csv"
        filepath = os.path.join(self.processed_dir, filename)
        try:
            df.to_csv(filepath, index=False)
            logging.info(f"Processed data successfully saved to: {filepath}")
            return filepath
        except Exception as e:
            logging.error(f"Failed to save processed data: {e}")
            raise

if __name__ == "__main__":
    transformer = FitnessDataTransformer()
    latest_raw = transformer.get_latest_raw_file()
    transformed_df = transformer.transform_data(latest_raw)
    transformer.save_processed_data(transformed_df)