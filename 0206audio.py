import streamlit as st
import json, requests
from PIL import Image
import random
from gtts import gTTS
     

st.title("WELCOME TO YOUR APHASIA APP!")
st.write("\n")
st.header("What do you see on the picture below?")
st.write("\n")
st.write("\n")


items = ['rabbit', 'car', 'tree', 'apple', 'table', 'tomato', 'door']
if 'item' not in st.session_state:
    rand_item = random.choice(items)
    st.session_state.item = rand_item
else:
    rand_item = st.session_state.item


picture = "images/" + rand_item + '.jpg'
img = Image.open(picture)
st.image(img, width=300)


user_input = st.text_input("Enter the word here")
    
if user_input:
    st.write("You entered:",user_input)
    if user_input.lower() == str(rand_item):
        st.write("Congratulations! You entered the correct word!")
    else:
        st.write("Unfortunately this is incorrect. Please try again or get a hint below.")
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
                    if user_input2.lower() == str(rand_item):
                        st.write("Super! Now you entered the correct word!")
                        st.write("Finally, let us speak the word together. Please press the play button below")
                        tts=gTTS(text= rand_item, lang='en')
                        tts.save('user.mp3')
                        st.audio('user.mp3')
                    else:
                        st.write("Incorrect again. The word starts with", rand_item[0])
                        user_input3 = st.text_input("Last chance, enter the word here")
                        if user_input3:
                          st.write("You entered:",user_input3)
                          if user_input3.lower() == str(rand_item):
                                        st.write("Super! Now you entered the correct word!")
                                        st.write("Finally, let us speak the word together. Please press the play button below")
                                        tts=gTTS(text= rand_item, lang='en')
                                        tts.save('user.mp3')
                                        st.audio('user.mp3')
                          else:
                            st.write("Unfortunately this is incorrect again. The word was: ", rand_item)
                            st.write("Nevertheless, let us speak the word togethet. Please press the play button below)
                            tts=gTTS(text= rand_item, lang='en')
                            tts.save('user.mp3')
                            st.audio('user.mp3')
                        
                        
                        
else:
    pass
