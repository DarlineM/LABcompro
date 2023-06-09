import streamlit as st
import json, requests
import random
from PIL import Image
from textblob import TextBlob


st.title("WELCOME TO YOUR APHASIA APP!")
st.write("\n")
st.header("What do you see on the picture below?")
st.write("\n")
st.write("\n")

items = ['to_eat', 'to_read', 'tree', 'apple']
if 'item' not in st.session_state:
    rand_item = random.choice(items)
    st.session_state.item = rand_item
else:
    rand_item = st.session_state.item

picture = "images/" + rand_item + '.jpg'
img = Image.open(picture)
st.image(img, width=300)

user_input = st.text_input("Enter the word")

if user_input:
    st.write("You entered:",user_input)
    if user_input.lower() == str(rand_item):
        st.write("You entered the correct word!")
        st.write("\n")
        blob = TextBlob(user_input.lower())
        correct_word = blob.correct()
        if correct_word == rand_item:
            st.write("Well done, you spelled the word correctly!")
        else:
            st.write("You spelled the word incorrectly. The correct spelling of the word is:", rand_item)
    else:
        st.write("Unfortunately ths is incorrect. Please try again or get a hint below.")
        st.write("\n")
        st.write("\n")
        option = st.selectbox("Choose one for help", ["None selected. Select your hint", "It is another word for", "It sounds like", "Similar in meaning to", "It rhymes with"])

        if option:
            key_dict = {"It is another word for": "rel_syn", "It sounds like": "sl", "Similar in meaning to": "ml", "It rhymes with": "rel_rhy"}
            key = key_dict[option] if option in key_dict else None

            if key:
                keyword = rand_item
                url = 'https://api.datamuse.com/words?' + key + "=" + keyword
                response = requests.get(url)
                dataFromDatamuse = json.loads(response.text)
                st.write(dataFromDatamuse[0]["word"])

                st.write("\n")
                st.write("Still no idea? Choose another hint!")
                st.write("\n")
                user_input2 = st.text_input("Or try again now and enter the word")
                if user_input2:
                    st.write("You entered:",user_input2)
                    if user_input.lower() == str(rand_item):
                        st.write("You entered the correct word!")
                        st.write("\n")
                        blob = TextBlob(user_input.lower())
                        correct_word = blob.correct()
                        if correct_word == rand_item:
                            st.write("Well done, you spelled the word correctly!")
                        else:
                            st.write("You spelled the word incorrectly, but it's close! The correct spelling is:", rand_item)
                    elif TextBlob(user_input.lower()).correct() == str(rand_item):
                     st.write("Close, but incorrect spelling! The correct spelling is:", rand_item)
                    else:
                     st.write("Unfortunately this is incorrect. Please try again or get a hint below.")
                     st.write("\n")
                     st.write("\n")
else:
    pass

if st.button("Reload app"):
  st.experimental_rerun()
        
