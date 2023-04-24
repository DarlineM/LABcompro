import streamlit as st
import json,requests
from PIL import Image
import random

#img = Image.open('apple.jpg')

#st.image(img)

items = ['to_eat', 'to_read', 'tree', 'apple']
rand_item = random.choice(items)
  
st.button(label='START', key = "<uniquevalueofsomesort>")
  #items = ['to_eat', 'to_read', 'tree', 'apple']
  #rand_item = random.choice(items)
picture = rand_item + '.jpg'
img = Image.open(picture)
st.image(img)

if st.button(label='HELP1'):
  keyword = rand_item
  key = "rel_syn"
  url= 'https://api.datamuse.com/words?' + key + "=" + keyword 
  response = requests.get(url)
  dataFromDatamuse = json.loads(response.text) 
  st.write(dataFromDatamuse)
  
  #option = st.selectbox("Choose one",("It is another word for", "It sounds like", 
                     #               "It means like", "It rhymes with"))
#if option:
 # elif option == "It is another word for":
  #  key ="rel_syn"
 # elif option == "It sounds like":
   # key = "sl"
 # elif option == "It means like":
  #  key = "ml"
 # elif option == "It rhymes with":
   # key = "rhy"
      
#  if(key and keyword):
 #   url= 'https://api.datamuse.com/words?' + key + "=" + keyword 
 #   response = requests.get(url)
  #  dataFromDatamuse = json.loads(response.text) 
  #  st.write(dataFromDatamuse)
        

      
        
