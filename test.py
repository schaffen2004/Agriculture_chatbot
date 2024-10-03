import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data_path = 'data/banana.csv'
df = pd.read_csv(data_path)

# Title and description
st.title('Banana Production EDA')
st.write("This app performs exploratory data analysis on the banana production dataset.")

# Display the raw data
st.header('Raw Data')
st.write(df)

# Summary statistics
st.header('Summary Statistics')
st.write(df.describe())

# Select columns for visualization
columns = df.columns[1:]  # Exclude the index column
selected_column = st.selectbox('Select a column to visualize', columns)

# Line plot of selected column over the years
st.subheader(f'{selected_column} Over Time')
fig, ax = plt.subplots()
sns.lineplot(x='Year', y=selected_column, data=df, ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)


# Filter data by year
st.header('Filter Data by Year')
year = st.slider('Select year', int(df['Year'].min()), int(df['Year'].max()))
filtered_data = df[df['Year'] == year]
st.write(filtered_data)



