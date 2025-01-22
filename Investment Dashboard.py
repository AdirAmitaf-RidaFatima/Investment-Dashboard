!pip install streamlit  # Install the streamlit library

import streamlit as st
import pandas as pd
import plotly.express as px

# Specify the file path
file_path = r"/content/tabula-PeriodicTradeSummaryReport.csv"

# Read the CSV file
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print(df.columns) # Print the column names to verify

# Assuming the column with profit and loss is named 'Amount' (check your CSV file)
# Change 'Net' to the actual column name:
fig = px.line(df, x='Amount', y='Security Name', title='Profit and Loss by each Company')  
fig.show()
st.plotly_chart(fig)