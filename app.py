import streamlit as st
from src.pipeline.predict_pipeline import CustomData, PredictionPipeline

def main():
    st.title("California House Prediction")
    
    # Create input elements
    latitude = st.number_input("Enter Latitude:", value=0.0)
    longitude = st.number_input("Enter Longitude:", value=0.0)
    housing_median_age = st.slider("Housing Median Age:", 0, 100, 50)
    total_rooms = st.number_input("Total Rooms:", value=0)
    total_bedrooms = st.number_input("Total Bedrooms:", value=0)
    population = st.number_input("Population:", value=0)
    households = st.number_input("Households:", value=0)
    median_income = st.number_input("Median Income:", value=0.0)
    ocean_proximity = st.selectbox("Ocean Proximity:", ["<Select>", "Near Bay", "Inland", "Ocean", "Near Ocean"])

    # Sidebar description
    st.sidebar.header("Description")
    st.sidebar.write("Made using Hands-On Machine Learning with Scikit-Learn book as reference")

    # Check if the user has provided all required inputs
    if st.button("Submit"):
        if (
            longitude != 0.0
            and latitude != 0.0
            and housing_median_age != 50
            and total_rooms != 0
            and total_bedrooms != 0
            and population != 0
            and households != 0
            and median_income != 0.0
            and ocean_proximity != "<Select>"
        ):
            # Create a CustomData object with user input
            custom_data = CustomData(
                longitude=longitude,
                latitude=latitude,
                housing_median_age=housing_median_age,
                total_rooms=total_rooms,
                total_bedrooms=total_bedrooms,
                population=population,
                households=households,
                median_income=median_income,
                ocean_proximity=ocean_proximity
            )
            
            # Example: You can use the custom_data object in your prediction pipeline
            prediction_pipeline = PredictionPipeline()
            predictions = prediction_pipeline.predict(custom_data)
            
            st.success("Input submitted successfully! You can process it further in your prediction pipeline.")
        else:
            st.error("Please provide all required inputs.")

if __name__ == "__main__":
    main()
