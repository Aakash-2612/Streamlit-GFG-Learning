import streamlit as st
from BMI import BMI_calculator
from Rating import rate

choice = st.sidebar.selectbox('Menu', ['BMI', 'Rate Yourself'])

if choice == 'BMI':
    BMI_calculator()
else:
    rate()
