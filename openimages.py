import streamlit as st
from PIL import Image

image = Image.open('apple.png')

st.image(image, caption='This is an apple')
