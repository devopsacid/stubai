import streamlit as st
from image_gen import generate_image

st.title("Image Generator")
description = st.text_input("Provide the description of the image:")

if st.button("Generate Image"):
    if description:
        with st.spinner('Generating image... Please wait'):
            image = generate_image(description)
        st.image(image, caption="Generated Image", use_column_width=True)
    else:
        st.warning("Please enter a description for the image.")