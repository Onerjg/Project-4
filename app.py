import streamlit as st
import pandas as pd
import plotly.express as px

#Loading the Data Set
df = pd.read_csv('vehicles_us.csv')

#Adding Header
st.header("Vehicle Data Dashboard")

#Displaying Data
st.write("This dashboard shows some exploratory data analysis of the vehicles in the dataset.")

#Adding Histrogram
fig_histogram = px.histogram(df, x='price', title='Distribution of Vehicle Prices')
st.plotly_chart(fig_histogram)

# Adding scatter plot
fig_scatter = px.scatter(df, x='odometer', y='price', title='Odometer vs. Vehicle Price')
st.plotly_chart(fig_scatter)

# Adding checkbox
show_expensive_cars = st.checkbox('Show only cars priced above $20,000')

if show_expensive_cars:
    filtered_df = df[df['price'] > 20000]
else:
    filtered_df = df

df['price'] = pd.to_numeric(df['price'], errors='coerce')
df.dropna(subset=['price'], inplace=True)

st.write(filtered_df)