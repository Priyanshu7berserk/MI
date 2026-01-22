import streamlit as st

st.title("basic calculator")


num1 = st.number_input("Enter first number ")
num2 = st.number_input("Enter second number ")

       
operation = st.selectbox("choose operations" , ["add","sub" ,"multiply" ,"divide"])                     
if st.button("calculate"):
    if operation == "add":
        st.write(num1 + num2)
    elif operation == "sub":
        st.write(num1 - num2)
    elif operation == "multiply":
        st.write(num1 * num2)
    elif operation == "divide":
        if num2 != 0:
            st.write(num1 / num2)  
        else:
            st.write("Error: Division by zero")
   