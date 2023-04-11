#! python3
from gtts import gTTS
import IPython.display as ipd  
from googletrans import Translator
import streamlit as st

translator = Translator()
word_user=st.text_input('Give some text:')

languageis = translator.translate(word_user, dest='de')

tts=gTTS(text=languageis.text, lang='de')
tts.save('user.mp3')
print('in german:')
st.audio('user.mp3')
