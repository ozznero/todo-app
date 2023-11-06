import streamlit as st
from PIL import Image

st.title("Camera Station")
st.subheader("In old-fashioned style")

uploaded_image = st.file_uploader("Upload Image to convert in grayscale")

if uploaded_image:
    # create a pillow image instance
    img_uploaded = Image.open(uploaded_image)
    # convert the pillow image to greyscale
    gray_img_uploaded = img_uploaded.convert("L")
    # render the grayscale image
    st.image(gray_img_uploaded)

with st.expander("Start the Camera"):
    # start the camera
    camera_image = st.camera_input("Camera")

if camera_image:
    # create a pillow image instance
    img = Image.open(camera_image)
    # convert the pillow image to greyscale
    gray_img = img.convert("L")
    # render the grayscale image
    st.image(gray_img)
