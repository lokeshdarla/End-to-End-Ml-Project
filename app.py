import streamlit as st
import pandas as pd
import sys
from src.exception import CustomException
from src.utils import load_object
from src.logger import logging
from src.pipeline.predict_pipeline import PredictionPipeline, CustomData  # Import the PredictionPipeline and CustomData classes

def main():
    st.title('California House Price Prediction')

    # Sidebar input fields
    longitude = st.sidebar.number_input('Longitude', value=0.0, step=0.01)
    latitude = st.sidebar.number_input('Latitude', value=0.0, step=0.01)
    housing_median_age = st.sidebar.number_input('Housing Median Age', value=0, step=1)
    total_rooms = st.sidebar.number_input('Total Rooms', value=0, step=1)
    total_bedrooms = st.sidebar.number_input('Total Bedrooms', value=0, step=1)
    population = st.sidebar.number_input('Population', value=0, step=1)
    households = st.sidebar.number_input('Households', value=0, step=1)
    median_income = st.sidebar.number_input('Median Income', value=0.0, step=0.01)
    ocean_proximity = st.sidebar.selectbox('Ocean Proximity', ['<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN'])

    custom_data = CustomData(longitude, latitude, housing_median_age, total_rooms, total_bedrooms,
                            population, households, median_income, ocean_proximity)

    if st.sidebar.button('Predict'):
        prediction_pipeline = PredictionPipeline()
        input_data = custom_data.get_data_as_dataframe()

        try:
            predictions = prediction_pipeline.predict(input_data)
            st.subheader('House Price Prediction')
            st.write(f'Predicted House Price: ${predictions[0]:,.2f}')
        except Exception as e:
            CustomException(e, sys)

if __name__ == '__main__':
    main()
