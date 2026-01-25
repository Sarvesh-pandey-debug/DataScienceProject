from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline

logger.info("wellcome to datascience custome logger")

STAGE_NAME = "Data ingestion stage"

try:
    logger.info(f"....... stage {STAGE_NAME}  started .......") 
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f"...... stage {STAGE_NAME}  completed ........\n\nx=======x")
except Exception as e:
    logger.exception(e)
    raise e           
        
