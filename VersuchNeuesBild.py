import streamlit as st

items = ['apple', 'to_eat', 'to_read', 'tree']

length = len(items)
i = 0

while i < length:
    st.write("test", items[i])
    user_input2 = st.text_input("Try again now! Enter the word")
    def clear_text():
      st.session_state["text"] = ""
    st.button("clear text input", on_click=clear_text)
    st.write(input)
    if user_input2.lower() == items[i]:
      st.write("Super! Now you entered the correct word!")
      i += 1
