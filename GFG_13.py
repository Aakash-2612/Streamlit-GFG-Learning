import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.subheader('Data Visualization with Seaborn and Matplotlib')
df = sns.load_dataset('iris')

st.dataframe(df, width=650)

st.text('1. Bar chart using Matplotlib')
fig = plt.figure(figsize=(15, 8))
df['species'].value_counts().plot(kind='bar')
st.pyplot(fig)

st.text('2. Pie chart using Matplotlib')
fig = plt.figure(figsize=(15, 8))
df['species'].value_counts().plot(kind='pie')
st.pyplot(fig)

st.text('3. Distplot using Seaborn')
fig = plt.figure(figsize=(15, 8))
sns.histplot(data=df['sepal_length'], alpha=0.4, stat='density', kde=True, kde_kws={"cut": 3})
st.pyplot(fig)

col1, col2 = st.columns(2)
with col1:
    col1.write('Hist = False')
    fig1 = plt.figure()
    sns.kdeplot(df['sepal_length'])
    st.pyplot(fig1)

with col2:
    col2.write('KDE = False')
    fig2 = plt.figure()
    sns.histplot(data=df['sepal_length'], kde=False, alpha=0.4, stat='density')
    st.pyplot(fig2)

st.text('4. Changing the Style of the Graph')
col1, col2 = st.columns(2)
with col1:
    fig1 = plt.figure()
    sns.set_style('darkgrid')
    sns.set_context('notebook')
    sns.kdeplot(df['sepal_length'])
    st.pyplot(fig1)

with col2:
    fig2 = plt.figure()
    sns.set_theme(context='poster', style='darkgrid')
    sns.kdeplot(df['sepal_length'])
    st.pyplot(fig2)

st.text('5. Scatter Plot')
fig, ax = plt.subplots(figsize=(15, 8))
ax.scatter(*np.random.random(size=(2, 100)))
st.pyplot(fig)

st.text('6. Count Plot')
fig = plt.figure(figsize=(15, 8))
sns.countplot(data=df, x='species')
st.pyplot(fig)

st.text('7. Box Plot')
fig = plt.figure(figsize=(15, 8))
sns.boxplot(data=df, x='species', y='petal_length')
st.pyplot(fig)

st.text('8. Violin Plot')
fig = plt.figure(figsize=(15, 8))
sns.violinplot(data=df, x='species', y='petal_length')
st.pyplot(fig)


