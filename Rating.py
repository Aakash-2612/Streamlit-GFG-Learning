import streamlit as st


def rate():
    with st.sidebar:
        st.title('Rate Yourself')
        languages = st.text_input('Enter the programming languages you know with comma separated', value='Python')
        languages = [i.strip() for i in languages.split(',')]

    st.subheader('How would you rate yourself in the following programming languages and tools?')

    for language in languages:
        st.write(language)
        st.slider(language, min_value=0., max_value=10., step=0.5)
