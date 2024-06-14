import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('abalone.csv')
st.subheader('1. Display DataFrame')
st.dataframe(df)

st.subheader('2. Display head of the DataFrame')
st.dataframe(df.head())

st.subheader('3. Display tail of the DataFrame')
st.dataframe(df.tail())

st.subheader('4. Display the DataFrame as Table(first 10 rows)')
st.table(df.head(10))

st.subheader('5. Display Json Data')
js = [{'pid': 1, 'name': 'Car'},
      {'pid': 2, 'name': 'Truck'},
      {'pid': 3, 'name': 'Bike'},
      {'pid': 4, 'name': 'Helicopter'},
      {'pid': 5, 'name': 'Aeroplane'}]
st.json(js)

st.table(df.describe())

