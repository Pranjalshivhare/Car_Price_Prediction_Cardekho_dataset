import dataclasses
import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np
model = pickle.load(open('carpricemodel.sav', 'rb'))

st.title('Car Price Prediction')
st.sidebar.header('Car Data')


# FUNCTION
def user_report():
    Present_Price = st.number_input('Present Price in Lakhs', 0.0, 10000000.0)
    # Present_Price = st.sidebar.slider('Present_Price_in_Lakhs', 1, 40, 1)
    Kms_Driven = st.number_input('KM Driven', 0, 10000000)

    # Kms_Driven = st.sidebar.slider('Kms_Driven', 1000, 100000, 1)
    Owner = st.sidebar.slider('Owner', 0, 1, 0)
    No_year = st.sidebar.slider('No_year', 0, 30, 0)
    Fuel_Type_Diesel = st.sidebar.slider('Fuel_Type_Diesel', 0, 1, 1)
    Fuel_Type_Petrol = st.sidebar.slider(
        'Fuel_Type_Petrol Year', 0, 1, 0)
    Seller_Type_Individual = st.sidebar.slider(
        'Seller_Type_Individual', 0, 1, 0)
    Transmission_Manual = st.sidebar.slider('Transmission_Manual', 0, 1, 0)

    user_report_data = {
        'Present_Price': Present_Price,
        'Kms_Driven': Kms_Driven,
        'Owner': Owner,
        'No_year': No_year,
        'Fuel_Type_Diesel': Fuel_Type_Diesel,
        'Fuel_Type_Petrol': Fuel_Type_Petrol,
        'Seller_Type_Individual': Seller_Type_Individual,
        'Transmission_Manual': Transmission_Manual
    }
    report_data = pd.DataFrame(user_report_data, index=[0])
    return report_data


user_data = user_report()
st.header('Car Data')
st.write(user_data)

salary = model.predict(user_data)
st.subheader('Car Price will be ')
st.subheader('Rs. '+str(np.round(salary[0], 2)) + 'as per the data.')

