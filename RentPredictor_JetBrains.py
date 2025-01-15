import streamlit as st
import pandas as pd
import numpy as np
import pickle
data= pd.read_csv('usable_data.csv')
df = pd.DataFrame(data)
st.title('Rent Predictor')

if 'city' and 'locality' in df.columns:
    options_1 = ['Select City...'] + sorted(df['city'].unique())
    city_option = st.selectbox('City', options_1)
    options_2 = ['Enter Locality...'] + sorted(df['locality'].unique())
    locality_option = st.selectbox('Locality', options_2)

if 'beds' in df.columns:
    options_3 = ['Enter Bedrooms...'] + sorted(df['beds'].unique())
    Beds_option = st.selectbox('Bedrooms', options_3)

if 'area' and 'area_rate' in df.columns:
    options_4 = ['Enter required area in square feet...'] + sorted(df['area'])
    Area_option = st.selectbox('Area', options_4)
    options_5 = ['Enter INR per square feet...'] + sorted(df['area_rate'])
    Budget_option = st.selectbox('Budget', options_5)


#Total_Price =
def predict(city, locality, area, beds, budget):

    input_data = pd.DataFrame(
        [[city, locality, area, beds, budget]],
        columns=["city", "locality", "area", "beds", "area_rate"]
    )

    with open("rent_predictor.pkl", "rb") as model_file:
        rent_predictor = pickle.load(model_file)

    prediction = rent_predictor.predict(input_data)
    return np.round(prediction[0],2)  # Return the predicted rent

if st.button("Predict Rent", type="primary"):
    try:
        result = predict(city_option, locality_option, Area_option, Beds_option, Budget_option)
        st.write(f"Your monthly rent will be: ₹{result}")
    except FileNotFoundError:
        st.error("Model file not found. Please ensure 'rent_predictor.pkl' exists.")
    except EOFError:
        st.error("The model file is corrupted or empty. Please recreate it.")
    except Exception as e:
        st.error(f"An error occurred: {e}")