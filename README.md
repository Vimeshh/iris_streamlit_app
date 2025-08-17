# Iris Streamlit App

## Overview
This is a simple machine learning web application built with **Streamlit**.  
It allows users to explore the Iris dataset, visualize data, and make real-time predictions using a trained ML model.

---

## Features
- **Dataset Overview**: View shape, columns, and data types  
- **Data Visualization**: Scatter plots, histograms, and correlation heatmaps  
- **Interactive Filtering**: Filter dataset interactively  
- **Model Prediction**: Input widget for predicting Iris species  
- **Prediction Display**: Show predicted class and confidence  
- **Model Performance**: Metrics and performance charts  

---

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



---

## How to Run Locally

1. **Clone the repository:**

git clone https://github.com/Vimeshh/iris_streamlit_app.git
cd iris_streamlit_app

2 .Create and activate a virtual environment:
conda create -n iris_env python=3.11
conda activate iris_env


3. Install dependencies:


pip install -r requirements.txt


4 Run the Streamlit app:

streamlit run app.py


Deployment

The app is deployed on Streamlit Cloud.
Access it here: Your Streamlit App URL
