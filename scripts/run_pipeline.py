import time
import logging
from extract import FitnessDataExtractor
from transform import FitnessDataTransformer
from load import FitnessDataDataLoader

# Configure logging for master pipeline orchestration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [MASTER-ELT] %(message)s",
    handlers=[logging.StreamHandler()]
)

def run_complete_elt_pipeline():
    start_time = time.time()
    logging.info("==================================================")
    logging.info("🚀 STARTING END-TO-END FITNESS-TECH ELT PIPELINE")
    logging.info("==================================================")

    try:
        # Step 1: Extraction
        logging.info("Step 1/3: Running Data Extraction...")
        extractor = FitnessDataExtractor()
        raw_payload = extractor.fetch_data()
        extractor.save_raw_data(raw_payload)
        logging.info("Step 1/3 Complete: Extraction successful.")

        # Step 2: Transformation
        logging.info("Step 2/3: Running Data Transformation...")
        transformer = FitnessDataTransformer()
        latest_raw = transformer.get_latest_raw_file()
        transformed_df = transformer.transform_data(latest_raw)
        transformer.save_processed_data(transformed_df)
        logging.info("Step 2/3 Complete: Transformation successful.")

        # Step 3: Loading
        logging.info("Step 3/3: Running Data Loading into DuckDB...")
        loader = FitnessDataDataLoader()
        latest_csv = loader.get_latest_processed_file()
        loader.load_data_to_duckdb(latest_csv)
        logging.info("Step 3/3 Complete: Loading successful.")

        elapsed_time = round(time.time() - start_time, 2)
        logging.info("==================================================")
        logging.info(f"✅ FULL ELT PIPELINE FINISHED SUCCESSFULLY in {elapsed_time} seconds.")
        logging.info("==================================================")

    except Exception as e:
        logging.error("❌ ELT PIPELINE FAILED!")
        logging.error(f"Error details: {e}")
        raise

if __name__ == "__main__":
    run_complete_elt_pipeline()