#! python3
from gtts import gTTS
from googletrans import Translator
import streamlit as st

translator = Translator()
word_user=st.text_input('Give some text:')
language=st.text_input('Type in a language')
languageis = translator.translate(word_user, dest=language)

tts=gTTS(text=languageis.text, lang=language)
tts.save('user.mp3')
print('in german:')
st.audio('user.mp3')
