import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff


st.title('Visualization with Plotly')
df = pd.read_csv('tips.csv')
st.dataframe(df.head(5))

st.text('1. Pie Chart type - 1')
fig = px.pie(df, values='total_bill', names='day')
st.plotly_chart(fig)

st.text('2. Pie Chart type - 2')
fig = px.pie(df, values='total_bill', names='day', opacity=.9, hole=.5,
             color_discrete_sequence=px.colors.sequential.RdBu)
st.plotly_chart(fig)

st.title('3. Multiple Dist_plots')
x1 = np.random.randn(200) + 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) - 2
hist_data = [x1, x2, x3]

group_lbs = ['G1', 'G2', 'G3']
fig = ff.create_distplot(hist_data, group_lbs, bin_size=[.1, .1, .1])
st.plotly_chart(fig, use_container_width=True)

fig = ff.create_distplot(hist_data, group_lbs, bin_size=[.1, .25, .5])
st.plotly_chart(fig, use_container_width=True)
