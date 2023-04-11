import json, requests
from googletrans import Translator
import streamlit as st

language = st.selectbox('Please, select destination language', ('it', 'de', 'en', 'fr'))
keyword = st.text_input('Insert a word')
translator = Translator()

if (language and keyword):
  translate = translator.translate(keyword, dest=language)
  st.write(translate.text)
