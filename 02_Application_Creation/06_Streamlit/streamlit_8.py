import streamlit as st # pip install streamlit

# text input
text_input = st.text_input("Introduce your name: ")
st.write("Your name is: ", text_input)

# int input
int_input = st.number_input("Introduce your age: ")
st.write("Your age is: ", int_input)
