import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show():
    # Load the data
    data_path = 'data/banana.csv'
    df = pd.read_csv(data_path)
    
    # Title and description
    st.title('Trực quan hoá dữ liệu về tình hình sản xuất chuối ở Việt Nam từ năm 1961 đến năm 2022')

    # Display the raw data
    st.header('Dữ liệu')
    st.write(df)

    # Summary statistics
    st.header('Thống kê')
    st.write(df.describe())

    # Select columns for visualization
    columns = df.columns[1:]  # Exclude the index column
    selected_column = st.selectbox('Vui lòng chọn đặc trưng để biểu diễn theo thời gian', columns)

    # Line plot of selected column over the years
    st.subheader(f'{selected_column} theo thời gian')
    fig, ax = plt.subplots()
    sns.lineplot(x='Year', y=selected_column, data=df, ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)


    # Filter data by year
    st.header('Lọc theo từng năm')
    year = st.slider('Chọn năm', int(df['Year'].min()), int(df['Year'].max()))
    filtered_data = df[df['Year'] == year]
    st.write(filtered_data)



