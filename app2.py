import streamlit as st


st.title("Kindly add city and age")
age=st.slider("select your age" , 1,100)
city = st.selectbox("select your city", ["Delhi","Mumbai","Dehradun","Chennai"])

if st.button("Submit"):
    st.write("age" , age)
    st.write("city", city)