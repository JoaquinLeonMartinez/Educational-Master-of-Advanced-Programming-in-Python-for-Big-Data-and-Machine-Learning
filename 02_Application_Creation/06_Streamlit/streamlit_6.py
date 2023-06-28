import streamlit as st # pip install streamlit

options = st.multiselect("Pick your favourites languages", ("C++", "Python", "Java", "C#"))

st.write("You selected: ", options)