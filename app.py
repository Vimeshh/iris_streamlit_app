import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("notebook/best_iris_model.joblib")

st.title("Iris Flower Prediction App")
st.write("Enter the features of the iris flower to predict its species:")

# User inputs
sepal_length = st.number_input("Sepal Length (cm)", 0.0, 10.0, 5.1)
sepal_width = st.number_input("Sepal Width (cm)", 0.0, 10.0, 3.5)
petal_length = st.number_input("Petal Length (cm)", 0.0, 10.0, 1.4)
petal_width = st.number_input("Petal Width (cm)", 0.0, 10.0, 0.2)

# Prediction button
if st.button("Predict"):
    prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    st.success(f"The predicted Iris species is: {prediction[0]}")
