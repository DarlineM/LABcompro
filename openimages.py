import streamlit as st
from PIL import Image

image = Image.open('apple.jpg')

st.image(image, caption='This is an apple')
