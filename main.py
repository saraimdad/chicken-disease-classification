from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = 'Data Ingestion Stage'
try:
    logger.info(f'>>>>>> {STAGE_NAME} Started <<<<<<')
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>> {STAGE_NAME} Completed <<<<<<\n\n')
except Exception as e:
    logger.exception(e)
    raise e  

STAGE_NAME = 'Preparing Base Model Stage'
try:
    logger.info(f'>>>>>> {STAGE_NAME} Started <<<<<<')
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>> {STAGE_NAME} Completed <<<<<<\n\n')
except Exception as e:
    logger.exception(e)
    raise e 
