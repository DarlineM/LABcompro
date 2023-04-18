import json,requests
import random
import streamlit as st
!pip install bing-image-downloader
from bing_image_downloader import downloader

st.start_button(label='START')
#oder?
if st.start_button(label='START'):

items = ['to eat', 'to read', 'summer', 'winter', 'tree', 'head', 'ear', 'apple']

rand_item = random.choice(items)

downloader.download(rand_item, limit=1,  output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)

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
