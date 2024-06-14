import streamlit as st

st.subheader("1. Radio Button")
gender = st.radio('Select your gender: ', options=('Male', 'Female', 'Others'), horizontal=True, help='Select any one')
st.write("You have selected: ", gender)

st.subheader("2. Select Box")
options = st.selectbox('Select your options: ', options=('Data Analysis', 'ML', 'DL', 'AI'), help='Select one')
st.write("You have selected: ", options)

st.subheader("3. Multi-Select Box")
st.multiselect('Select your options: ', options=('Data Analysis', 'ML', 'DL', 'AI'), help='Choose any', default='ML')

st.subheader("4. Button")
if st.button('Say Hello'):
    st.write("Hii")

st.subheader("5. Check-Box")
if st.checkbox('I agree to the terms and conditions.', help='you must agree to proceed'):
    st.write("Thank you")

st.subheader("6. Color Picker")
color = st.color_picker('Select your favorite color : ', '#08F318')
st.write("You have selected ", color, 'color')

st.button('Submit your response')

