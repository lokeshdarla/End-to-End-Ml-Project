import os
import sys
import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainerConfig,ModelTrainer

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# Calculate the project root directory and add it to sys.path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

# Import CustomException from the correct path
from src.exception import CustomException

# Path to the CSV data file
script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(script_dir, '..', '..', 'data', 'raw', 'housing.csv')

# Data class for configuration
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Enter the data ingestion method or component")
        try:
            df = pd.read_csv(data_dir)
            logging.info("Read the dataset as a DataFrame")

            # Create directories if they don't exist
            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path), exist_ok=True)

            # Save the raw data
            df.to_csv(self.data_ingestion_config.raw_data_path, index=False)

            logging.info("Train-test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save the train and test data
            train_set.to_csv(self.data_ingestion_config.train_data_path, index=False)
            test_set.to_csv(self.data_ingestion_config.test_data_path, index=False)

            logging.info("Ingestion of Data is completed")

            return {
                self.data_ingestion_config.train_data_path,
                 self.data_ingestion_config.test_data_path
            }
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    train_path,test_path=obj.initiate_data_ingestion()
    
    data_transformation=DataTransformation()
    train_array,test_array,preprocessed_path=data_transformation.initiate_data_transformation(train_path,test_path)

    model_trainer=ModelTrainer()
    model_trainer.initiate_model_trainer(train_array=train_array,test_array=test_array)