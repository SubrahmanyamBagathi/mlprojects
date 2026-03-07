

import os
import sys

from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifact','train.csv')
    test_data_path : str = os.path.join('artifact','test.csv')
    raw_data_path : str = os.path.join('artifact','raw_data.csv')
    
class DataConfig:
    def __init__(self):
        self.Ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv("notebook\data\stud.csv")
            logging.info("Read the Dataset as DataFrame")
            
            os.makedirs(os.path.dirname(self.Ingestion_config.train_data_path),exist_ok=True)
            
            df.to_csv(self.Ingestion_config.raw_data_path,index=False,header=True)
            
            logging.info("train test split intiated")
            train_set,test_test = train_test_split(df,test_size=0.2,random_state=42)
            
            train_set.to_csv(self.Ingestion_config.train_data_path,index=False,header=True)
            test_test.to_csv(self.Ingestion_config.test_data_path,index=False,header=True)
            
            logging.info("Ingestion of the data is completed")
            
            return(
                self.Ingestion_config.train_data_path,
                self.Ingestion_config.test_data_path
            )
            
        except Exception as e:
            raise CustomException(e,sys)


if __name__ == "__main__":
    obj = DataConfig()
    train_data,test_data = obj.initiate_data_ingestion()
    
    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data,test_data)
    
