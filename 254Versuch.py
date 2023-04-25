import streamlit as st
import json,requests
from PIL import Image
import random

img = Image.open('images/brainstorm.jpg')
st.image(img)

items = ['to_eat', 'to_read', 'tree', 'apple']
rand_item = random.choice(items)

picture = "images/" + rand_item + '.jpg'
img = Image.open(picture)
st.image(img, width = 300)

st.write("\n")
st.write("\n")

option = st.multiselect("Choose one",["It is another word for", "It sounds like",
"Similar in meaning to", "It rhymes with"])

if option == []:
  st.stop()

key_dict = {"It is another word for": "rel_syn",
"It sounds like": "sl",
"Similar in meaning to": "ml",
"It rhymes with": "rel_rhy"}

if option:
 if option == "It is another word for":
  key ="rel_syn"
 elif option == "It sounds like":
  key = "sl"
 elif option == "It means like":
  key = "ml"
 elif option == "It rhymes with":
  key = "rhy"

  if(key and keyword):
    url= 'https://api.datamuse.com/words?' + key + "=" + keyword
    response = requests.get(url)
    dataFromDatamuse = json.loads(response.text)
    st.write(dataFromDatamuse)
