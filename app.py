import streamlit as st

def main():
    st.title("Input Form")

    # Create input elements
    longitude = st.number_input("Enter Longitude:", value=0.0)
    latitude = st.number_input("Enter Latitude:", value=0.0)
    housing_median_age = st.slider("Housing Median Age:", 0, 100, 50)
    total_rooms = st.number_input("Total Rooms:", value=0)
    total_bedrooms = st.number_input("Total Bedrooms:", value=0)
    population = st.number_input("Population:", value=0)
    households = st.number_input("Households:", value=0)
    median_income = st.number_input("Median Income:", value=0.0)
    ocean_proximity = st.selectbox("Ocean Proximity:", ["<Select>", "Near Bay", "Inland", "Ocean", "Near Ocean"])

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
            # Process the user input or perform any desired actions here
            st.success("Input submitted successfully!")
        else:
            st.error("Please provide all required inputs.")

if __name__ == "__main__":
    main()
