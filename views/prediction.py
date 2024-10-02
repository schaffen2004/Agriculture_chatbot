import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error

def show():
# Load the dataset
    data = pd.read_csv('data/banana.csv')

    # Streamlit app title
    st.title("Dự đoán thông tin liên quan về tình hình sản xuất chuối ở Việt Nam")

    # Select the feature to predict
    feature = st.selectbox("Vui lòng chọn thông tin muốn dự đoán:", data.columns[3:])

    # Select the Machine Learning model
    model_choice = st.selectbox("Vui lòng chọn mô hình để dự đoán:", ["Linear Regression", "Random Forest", "Support Vector Regressor"])

    # Prepare data for training
    X = data[['Year']]  # Use 'Year' for time-based prediction
    y = data[feature].fillna(0)  # Fill missing values if any

    # Model selection
    if model_choice == "Linear Regression":
        model = LinearRegression()
    elif model_choice == "Random Forest":
        model = RandomForestRegressor()
    else:
        model = SVR()

    # Train the model
    model.fit(X, y)


    # Predict for a given year
    year_input = st.number_input("Chọn năm muốn đưa ra:", min_value=2023, max_value=2030, value=2025)
    year_pred = model.predict([[year_input]])
    st.write(f"Dự đoán {feature} cho {year_input}: {year_pred[0]:.2f}")
