import numpy as np
import pandas as pd
import os


script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(script_dir, '..', '..', 'data/preprocessed_data/train.csv')

from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.base import BaseEstimator, TransformerMixin
import joblib
rooms_ix, bedrooms_ix, population_ix, households_ix = 3, 4, 5, 6

class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room = True):
        self.add_bedrooms_per_room = add_bedrooms_per_room
    def fit(self, X, y=None):
        return self # nothing else to do
    def transform(self, X, y=None):
        rooms_per_household = X[:, rooms_ix] / X[:, households_ix]
        population_per_household = X[:, population_ix] / X[:, households_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household,
             bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]
        
df=pd.read_csv(data_dir,index_col=0)
housing = df.drop("median_house_value", axis=1)
housing_num =housing.drop('ocean_proximity',axis=1)

num_pipeline=Pipeline([
    ('imputer',SimpleImputer(strategy='median')),
    ('attrib_adder',CombinedAttributesAdder()),
    ('scaler',StandardScaler())
    
])

num_attribs = list(housing_num)
cat_attribs = ["ocean_proximity"]

full_pipeline=ColumnTransformer([
    ("num",num_pipeline,num_attribs),
    ("cat",OneHotEncoder(),cat_attribs)
])


# Build the path to the models directory
models_dir = os.path.join(script_dir, '..', '..', 'models')

# Create the full path for saving the pipeline

pipeline_path = os.path.join(models_dir, 'preprocessing_pipeline.pkl')
joblib.dump(full_pipeline, pipeline_path)