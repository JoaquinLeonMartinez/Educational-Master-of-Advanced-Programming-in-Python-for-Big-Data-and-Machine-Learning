import streamlit as st # pip install streamlit

option = st.selectbox("Pick your favourite language", ("C++", "Python", "Java"))

st.write("You selected: ", option)