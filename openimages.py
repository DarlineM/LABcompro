import streamlit as st
from PIL import Image
import random

#img = Image.open('apple.jpg')

#st.image(img)

if st.start_button(label='START'):
  items = ['to_eat', 'to_read', 'tree', 'apple']
  rand_item = random.choice(items)
  picture = rand_item + '.jpg'
  img = Image.open(picture)
  st.image(img)
