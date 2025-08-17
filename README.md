# Iris Streamlit App

## Overview
This is a simple machine learning web application built with Streamlit. It allows users to explore the Iris dataset, visualize data, and make real-time predictions using a trained model.

## Features
- Dataset overview (shape, columns, data types)
- Data visualization: scatter plots, histograms, and correlation heatmaps
- Interactive filtering of dataset
- Input widget for predicting Iris species
- Display prediction and confidence
- Model performance metrics and visualization

## Project Structure

iris_streamlit_app/
├── app.py # Main Streamlit app
├── requirements.txt # Dependencies
├── notebooks/
│ └── model_training.ipynb # Model training notebook
├── model/
│ └── best_iris_model.joblib # Trained ML model
├── data/
│ └── iris.csv # Dataset (optional)
└── README.md # Project documentation


How to Run Locally 
1. Clone the repository:

bash
git clone https://github.com/Vimeshh/iris_streamlit_app.git
cd iris_streamlit_app


Create and activate a virtual environment:

conda create -n iris_env python=3.11
conda activate iris_env


Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run app.py

Deployment

The app is deployed on Streamlit Cloud. Access it here:
Your Streamlit App URL

Authors

Vimesh Gunasekaran

License

