import streamlit as st
import pandas as pd
from PIL import Image

st.title('File Uploading')

# 1. Image
st.subheader('1. Uploading an image')
img_file = st.file_uploader('Upload Image', type=['png', 'jpg', 'jpeg'])
if img_file is not None:
    file_details = {'file_name': img_file.name, 'file_type': img_file.type, 'file_size': img_file.size}
    st.write(file_details)

    st.image(Image.open(img_file))

# 2. Audio
st.subheader('2. Uploading an Audio')
audio_file = st.file_uploader('Upload Image', type=['mp3', 'wav'])
if audio_file is not None:
    file_details = {'file_name': audio_file.name, 'file_type': audio_file.type, 'file_size': audio_file.size}
    st.write(file_details)
    st.audio(audio_file)

# 3. Video
st.subheader('3. Uploading an Video')
img_file = st.file_uploader('Upload Video', type=['mp4', 'mov'])
if img_file is not None:
    file_details = {'file_name': img_file.name, 'file_type': img_file.type, 'file_size': img_file.size}
    st.write(file_details)

    st.video(img_file)

# 4. CSV
st.subheader('4. Uploading an CSV')
img_file = st.file_uploader('Upload CSV', type=['csv'])
if img_file is not None:
    file_details = {'file_name': img_file.name, 'file_type': img_file.type, 'file_size': img_file.size}
    st.write(file_details)

    st.dataframe(img_file)