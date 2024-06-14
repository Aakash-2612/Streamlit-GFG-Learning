import streamlit as st

# Title
st.title("Title - GFG")

# Header
st.header("Header - GFG")

# Subheader
st.subheader("Subheader - GFG")

# Text
st.text("Text - GFG")

# Markdown
st.markdown('This is a markdown text')  # p
st.markdown('# GFG')        # h1
st.markdown('## GFG')       # h2
st.markdown('### GFG')      # h3
st.markdown('#### GFG')     # h4
st.markdown('##### GFG')    # h5
st.markdown('###### GFG')   # h6

st.markdown('### **GFG**')  # h3 + bold
st.markdown('### __GFG__')  # h3 + bold

st.markdown('### *GFG*')  # h3 + italic
st.markdown('### _GFG_')  # h3 + italic

st.markdown('### ***GFG***')  # h3 + italic + bold
st.markdown('### ___GFG___')  # h3 + italic + bold

st.markdown('- First Point')
st.markdown('- Second Point')

st.write("Normal text")
st.write(range(1, 10))
