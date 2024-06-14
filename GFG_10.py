import streamlit as st
from PIL import Image
# streamlit run GFG_10.py --server.enableXsrfProtection false


def convert_image(image_path, new_format):
    with Image.open(image_path) as img:
        new_name = image_path.name.split('.')[0] + '.' + new_format
        final_path = 'C:\\Users\\aakas\\PycharmProjects\\Streamlit\\' + new_name
        img = img.convert('RGB')
        st.subheader(final_path)
        img.save(final_path)
        st.success('Image saved successfully at ' + final_path)


st.title('Image Converter')
image_path = st.file_uploader('Upload your image', type=['jpg', 'png', 'jpeg'])
new_format = st.selectbox('Select the output format', ['png', 'jpg', 'jpeg'])

if st.button('Convert'):
    if image_path is not None:
        convert_image(image_path, new_format)
    else:
        st.error("Please upload an image")
