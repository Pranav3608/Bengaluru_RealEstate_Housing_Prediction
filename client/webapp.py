import streamlit as st
import requests
from pydantic import BaseModel

# Define the PredictionRequest model
class PredictionRequest(BaseModel):
    total_sqft: float
    location: str
    bhk: int
    bath: int

# Streamlit app title
st.title('Bengaluru Real Estate Price Prediction')
st.text("Trouble buying & Selling property in Bengaluru? We got you covered!")

# Input fields for total square feet, BHK, and bathrooms
total_sqft = st.number_input('Property Size')
bhk = st.number_input('Select BHK')
bath = st.number_input('Number of Bathrooms')

# Dropdown to select location
response = requests.get('http://127.0.0.1:8000/get_location_names')
if response.status_code == 200:
    locations = response.json()['locations']
    location = st.selectbox('Select Location', options=locations)
else:
    st.error('Error fetching locations.')

# Button to trigger prediction
if st.button('Predict'):
    # Prepare the request data
    request_data = PredictionRequest(
        total_sqft=total_sqft,
        location=location,
        bhk=bhk,
        bath=bath
    )
    
    # Send request to FastAPI server for prediction
    response = requests.post('http://127.0.0.1:8000/predict_home_price', json=request_data.dict())
    
    # Display prediction result
    if response.status_code == 200:
        result = response.json()
        estimated_price = result['estimated_price']
        st.success(f'Estimated Price: {estimated_price}')
    else:
        st.error('Error occurred while fetching prediction.')
