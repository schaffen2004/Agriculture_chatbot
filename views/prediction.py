import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.statespace.sarimax import SARIMAX

def show():
    # Load the dataset
    data = pd.read_csv('data/banana.csv')

    # Streamlit app title
    st.title("Dự đoán thông tin liên quan về tình hình sản xuất quả chuối ở Việt Nam")

    # Select the feature to predict
    feature = st.selectbox("Vui lòng chọn thông tin muốn dự đoán:", data.columns[1:])

    # Select the Machine Learning model
    model_choice = st.selectbox("Vui lòng chọn mô hình để dự đoán:", 
                                 ["Linear Regression", "Random Forest", "Support Vector Regressor", "ARIMA", "SARIMA", "Exponential Smoothing"])

    # Prepare data for training
    X = data[['Year']]  # Use 'Year' for time-based prediction
    y = data[feature].fillna(0)  # Fill missing values if any

    # Model selection and prediction
    year_input = st.number_input("Chọn năm muốn đưa ra:", min_value=2023, max_value=2030, value=2025)

    # Khởi tạo biến year_pred
    year_pred = None

    # Model selection and prediction
    if model_choice == "Linear Regression":
        model = LinearRegression()
        model.fit(X, y)
        year_pred = model.predict([[year_input]])[0]  # Lấy giá trị đầu tiên

    elif model_choice == "Random Forest":
        model = RandomForestRegressor()
        model.fit(X, y)
        year_pred = model.predict([[year_input]])[0]  # Lấy giá trị đầu tiên

    elif model_choice == "Support Vector Regressor":
        model = SVR()
        model.fit(X, y)
        year_pred = model.predict([[year_input]])[0]  # Lấy giá trị đầu tiên

    elif model_choice == "ARIMA":
        model = ARIMA(y, order=(1, 1, 1))  # Thay đổi tham số cho ARIMA tùy theo dữ liệu của bạn
        model_fit = model.fit()
        year_pred = model_fit.forecast(steps=10).iloc[year_input-2022-1]  # Lấy giá trị đầu tiên bằng iloc

    elif model_choice == "SARIMA":
        model = SARIMAX(y, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))  # Thay đổi tham số tùy theo dữ liệu
        model_fit = model.fit()
        year_pred = model_fit.forecast(steps=10) .iloc[year_input-2022-1]  # Lấy giá trị đầu tiên bằng iloc

    elif model_choice == "Exponential Smoothing":
        model = ExponentialSmoothing(y, trend='add', seasonal='add', seasonal_periods=12)  # Điều chỉnh tham số theo dữ liệu
        model_fit = model.fit()
        year_pred = model_fit.forecast(steps=10).iloc[year_input-2022-1]  # Lấy giá trị đầu tiên bằng iloc


    # Output predictions
    data_2022 = data[data['Year'] == 2022][feature].values[0]
    mean_years = data[feature].mean()

    st.metric("Dự đoán", f"{year_pred:.4f}", f"{year_input}")
    st.metric("So với năm 2022", f"{(year_pred - data_2022):.4f}", f"{((year_pred - data_2022) * 100 / data_2022):.4f} %")
    st.metric("So với trung bình các năm", f"{(year_pred - mean_years):.4f}", f"{((year_pred - mean_years) * 100 / mean_years):.4f} %")

