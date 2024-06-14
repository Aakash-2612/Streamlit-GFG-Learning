import streamlit as st
from PIL import Image
import numpy as np
import cv2 as cv
# streamlit run GFG_11.py --server.enableXsrfProtection false

def rotate_image(image, angle):
    img = np.array(image)
    height, width = img.shape[:2]
    M = cv.getRotationMatrix2D((width / 2, height / 2), angle, 1)
    rotated_image = cv.warpAffine(img, M, (width, height))
    return rotated_image


st.title('Image Rotator')
st.subheader('Upload an image file : ')
img_file = st.file_uploader("Upload you image", type=['jpg', 'png', 'jpeg'])

st.subheader('Rotate the Image : ')
angle = st.slider('Choose the Angle : ', -180, 180, 0, 1)

if img_file is not None:
    image = Image.open(img_file)
    rotated_image = rotate_image(image, angle)
    st.image(rotated_image)

