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

    # Calculate percentage of missing and non-missing data
    missing_percentage = df.isnull().mean() * 100
    non_missing_percentage = 100 - missing_percentage

    # Data for the stacked bar chart
    data = pd.DataFrame({
        'Missing': missing_percentage,
        'Non-Missing': non_missing_percentage
    })

    st.title("Giá trị bị thiếu")
    st.write(missing_percentage[missing_percentage > 0].round(2))
    # Stacked bar chart of missing values
    st.header('Biểu đồ biểu thị giá trị bị thiếu theo phần trăm (%)')
    fig, ax = plt.subplots(figsize=(10, 6))
    data.plot(kind='bar', stacked=True, ax=ax, color=['red', 'green'])
    plt.ylabel('Phần trăm (%)')
    plt.title('Số lượng giá trị bị thiếu by Column')
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)

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
