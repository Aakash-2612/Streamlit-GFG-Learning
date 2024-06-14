import streamlit as st
from PIL import Image

# Image
st.title('1. Image from Path')
img = Image.open('C:\\Users\\aakas\\OneDrive\\Pictures\\Round2\\Tony_Stark.jpg')
st.image(img, width=600)

st.title('2. Image from Link')
st.image('https://media.geeksforgeeks.org/gfg-gg-logo.svg', width=600)

# Video
st.title('3. Video')
video_file = open('video.mp4', 'rb')
st.video(video_file, start_time=20)

# Audio
st.title('4. Audio')
audio_file = open('sample.mp3', 'rb')
st.audio(audio_file.read())
