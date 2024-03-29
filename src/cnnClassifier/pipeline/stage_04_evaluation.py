from cnnClassifier.components.evaluation import Evaluation
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier import logger

STAGE_NAME = 'Evaluation Stage'

class EvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()
 
if __name__ == '__main__':
    try:
        logger.info(f'>>>>>> {STAGE_NAME} Started <<<<<<')
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f'>>>>>> {STAGE_NAME} Completed <<<<<<\n\n')
    except Exception as e:
        logger.exception(e)
        raise e  