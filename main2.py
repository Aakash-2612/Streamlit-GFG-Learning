import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import altair as alt
import graphviz as graphviz
import base64
import pickle

# rand = np.random.normal(1, 2, size=20)
# fig, ax = plt.subplots()
# ax.hist(rand, bins=15)
# st.pyplot(fig)

# df = pd.DataFrame(
#     np.random.randn(10, 2),
#     columns=['x', 'y']
# )
# # print(df)
# st.bar_chart(df)

# st.graphviz_chart(
#     '''
#     digraph {
#     A -> B
#     C -> D
#     E -> F
#     F -> A
#     }
# ''')

df = pd.DataFrame(
    np.random.randn(500, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(df)
