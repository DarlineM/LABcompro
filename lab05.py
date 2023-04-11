import json, requests
from googletrans import Transloator
import streamlit as st

language = st.selectbox('Please, select destination language')
keyword = st.text_input('Insert a word')
translator = Translator()

if (language and keyword):
  translate = translator.translate(keyword, dest=language)
  st.write(translate.text)
