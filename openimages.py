import streamlit as st
from PIL import Image
import random

#img = Image.open('apple.jpg')

#st.image(img)

items = ['to eat', 'to read', 'tree', 'apple']

rand_item = random.choice(items)

picture = rand_item + '.jpg'

img = Image.open(picture)

st.image(img)
