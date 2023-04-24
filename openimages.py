import streamlit as st
from PIL import Image
import random

#img = Image.open('apple.jpg')

#st.image(img)
items = ['to_eat', 'to_read', 'tree', 'apple']
rand_item = random.choice(items)

if st.button(label='START'):
  #items = ['to_eat', 'to_read', 'tree', 'apple']
  #rand_item = random.choice(items)
  picture = rand_item + '.jpg'
  img = Image.open(picture)
  st.image(img)
  
keyword = rand_item
option = st.selectbox("Choose one",("It is another word for", "It sounds like", 
                                    "It means like", "It rhymes with"))
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
    st.write(datafromDatamuse)
