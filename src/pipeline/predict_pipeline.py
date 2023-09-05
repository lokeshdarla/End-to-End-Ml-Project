import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
from src.logger import logging
class PredictionPipeline:
    def __init__(self):
        pass
    
    def predict(self,features):
        try:
            model_path="artifacts/model.pkl"
            preprocessor_path="artifacts/preprocessor.pkl"
            logging.info("Before loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            logging.info("After loading")
            data_scaled=preprocessor.transform(features)
            predictions=model.predict(data_scaled)
            logging.info("Prediction completed")
            return predictions
        except Exception as e:
            CustomException(e,sys)
        
class CustomData:
    def __init__(self, longitude: int, latitude: int, housing_median_age: int, total_rooms: int, total_bedrooms: int, population: int, households: int, median_income: int, ocean_proximity: str):
        self.longitude = longitude
        self.latitude = latitude
        self.housing_median_age = housing_median_age
        self.total_rooms = total_rooms
        self.total_bedrooms = total_bedrooms
        self.population = population
        self.households = households
        self.median_income = median_income
        self.ocean_proximity = ocean_proximity

    def get_data_as_dataframe(self):
        try:
            custom_data_dict = {
                "longitude": [self.longitude],
                "latitude": [self.latitude],
                "housing_median_age": [self.housing_median_age],
                "total_rooms": [self.total_rooms],
                "total_bedrooms": [self.total_bedrooms],
                "population": [self.population],
                "households": [self.households],
                "median_income": [self.median_income],
                "ocean_proximity": [self.ocean_proximity],
            }

            return pd.DataFrame(custom_data_dict)
        except Exception as e:
            CustomException(e,sys)

    