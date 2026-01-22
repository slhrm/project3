import streamlit as st

st.title("Log in система")
name = st.text_input("Въведи име")
if st.button("Провери"):
if name.strip()=="":
  st.warning("Моля въведи текст")
  elif not name.isalpha():
  st.warning(".......")
  else st.success("Текстът е въведен правилно")
  
