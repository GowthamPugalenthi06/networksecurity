from networksecurity.components.data_ingestion import DataIngestion 
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import sys 
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig


if __name__=='__main__':
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(data_ingestion_config)
        logging.info("Initiated a data ingestion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)
    except Exception as e:
           raise NetworkSecurityException(e,sys)