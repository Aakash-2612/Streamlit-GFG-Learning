import time
import numpy as np
import pandas as pd
import streamlit as st
import emoji

st.set_page_config(page_title='GeeksForGeeks', layout='wide')
cases = []
for i in range(100):
    cases.append(np.random.randint(1, 7))

d = {}
for i in range(1, 7):
    d[i] = cases.count(i)

st.subheader('Frequency of getting a number on a die')

tab1, tab2 = st.tabs(['chart', 'data'])
with tab2:
    st.subheader('Die Tossed 100 times')
    st.write(d)
with tab1:
    st.bar_chart({key: value for key, value in d.items()})

with st.expander('See Explanation'):
    st.write('''
    The chart shows the output of the die tossed 100 times and
    It shows how many times each number appears
    ''')
    st.image('https://static.streamlit.io/examples/dice.jpg')

# with st.empty():
#     st.write('You need to wait for 10seconds')
#     for seconds in range(11):
#         st.write(str(seconds) + ' seconds remaining')
#         time.sleep(1)
#
#     st.write('10 seconds completed')

with st.spinner('Wait for it'):
    time.sleep(3)
    st.write('Thanks for being patient')

with st.empty():
    for percent_completed in range(100):
        time.sleep(.01)
        st.progress(percent_completed + 1, text='Processing...')
    st.success('Congratulations!')

st.balloons()

