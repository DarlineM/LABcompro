import streamlit as st
from PIL import Image

img = Image.open('apple.jpg')

st.image(img)
