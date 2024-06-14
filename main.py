import streamlit as st
import time

st.write("Hello, I am Aakash")
st.title("Aakash")
st.header("This is a the header")
st.slider("Pick a number", 0, 50)
st.button("Click")
st.selectbox("Pick", ['Male', 'Female'])
st.multiselect("Pick", ['Jupiter', 'Mars', 'Earth'])
st.select_slider("Pick", ['bad', 'average', 'Excellent'])
st.balloons()
st.progress(10)
st.snow()
with st.spinner('Wait for it...'):
    time.sleep(10)

st.sidebar.title("Hello")

