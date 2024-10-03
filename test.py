import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data_path = 'data/banana.csv'
df = pd.read_csv(data_path)

# Title
st.title('Missing Data Analysis')

# Display raw data
st.header('Raw Data')
st.write(df)

# Calculate percentage of missing and non-missing data
missing_percentage = df.isnull().mean() * 100
non_missing_percentage = 100 - missing_percentage

# Data for the stacked bar chart
data = pd.DataFrame({
    'Missing': missing_percentage,
    'Non-Missing': non_missing_percentage
})

st.title("Missing value")
st.write(missing_percentage[missing_percentage > 0].round(2))
# Stacked bar chart of missing values
st.header('Stacked Bar Chart of Missing Values (%)')
fig, ax = plt.subplots(figsize=(10, 6))
data.plot(kind='bar', stacked=True, ax=ax, color=['red', 'green'])
plt.ylabel('Percentage (%)')
plt.title('Missing vs Non-Missing Data by Column')
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)

# Conclusion
st.write("The stacked bar chart represents the percentage of missing and non-missing data for each column.")

