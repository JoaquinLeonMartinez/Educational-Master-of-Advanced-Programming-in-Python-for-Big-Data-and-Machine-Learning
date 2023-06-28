import streamlit as st # pip install streamlit

check = st.checkbox("Python")

if check:
    st.write("Good choice bro")
else:
    st.write("Are you sure?")