import numpy as np
import streamlit as st
import pandas as pd

st.title('1. Line Chart')
chart_data = pd.DataFrame(np.random.uniform(-2, 2, size=[20, 3]), columns=['L-1', 'L-2', 'L-3'])

tab1, tab2 = st.tabs(['Line Chart', 'Data'])

with tab1:
    st.line_chart(chart_data)
with tab2:
    st.dataframe(chart_data, width=350)

st.title('2. Area Chart')
tab1, tab2 = st.tabs(['Area Chart', 'Data'])

with tab1:
    st.area_chart(chart_data)
with tab2:
    st.dataframe(chart_data, width=350)

st.title('3. Bar Chart')
tab1, tab2 = st.tabs(['Bar Chart', 'Data'])

with tab1:
    st.bar_chart(chart_data)
with tab2:
    st.dataframe(chart_data, width=350)

