import streamlit as st 

st.title("few more featured added")

name = st.text_input("enter your name")

if st.button("submit"):
    st.write(f"hello,name")

