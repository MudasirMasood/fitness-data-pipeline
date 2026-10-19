import os
import json
import logging
import requests
from datetime import datetime
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

load_dotenv()

class FitnessDataExtractor:
    def __init__(self):
        self.api_url = "https://jsonplaceholder.typicode.com/users"
        self.output_dir = "data/raw"
        os.makedirs(self.output_dir, exist_ok=True)

    def fetch_data(self) -> list:
        logging.info(f"Initiating extraction from endpoint: {self.api_url}")
        try:
            response = requests.get(self.api_url, timeout=15)
            response.raise_for_status()
            data = response.json()
            logging.info(f"Successfully extracted {len(data)} records from source.")
            return data
        except requests.exceptions.RequestException as e:
            logging.error(f"API extraction failed: {e}")
            raise

    def save_raw_data(self, data: list) -> str:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"raw_fitness_telemetry_{timestamp}.json"
        filepath = os.path.join(self.output_dir, filename)
        try:
            with open(filepath, "w") as f:
                json.dump(data, f, indent=4)
            logging.info(f"Raw data successfully landed at: {filepath}")
            return filepath
        except Exception as e:
            logging.error(f"Failed to write raw file: {e}")
            raise

if __name__ == "__main__":
    extractor = FitnessDataExtractor()
    raw_payload = extractor.fetch_data()
    extractor.save_raw_data(raw_payload)