from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.datascience.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline


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
        
        
STAGE_NAME = "Data validation stage"

try:
    logger.info(f"....... stage {STAGE_NAME}  started .......") 
    obj = DataValidationTrainingPipeline()
    obj.initiate_data_validation()
    logger.info(f"...... stage {STAGE_NAME}  completed ........\n\nx=======x")
except Exception as e:
    logger.exception(e)
    raise e         


STAGE_NAME = "Data transformation stage"

if __name__== '__main__':
    try:
        logger.info(f"....... stage {STAGE_NAME}  started .......") 
        data_ingestion = DataTransformationTrainingPipeline()
        data_ingestion.initiate_data_transformation()
        logger.info(f"...... stage {STAGE_NAME}  completed ........\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model Trainer stage"

if __name__== '__main__':
    try:
        logger.info(f"....... stage {STAGE_NAME}  started .......") 
        obj = ModelTrainerTrainingPipeline()
        obj.initiate_model_training()
        logger.info(f"...... stage {STAGE_NAME}  completed ........\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e
