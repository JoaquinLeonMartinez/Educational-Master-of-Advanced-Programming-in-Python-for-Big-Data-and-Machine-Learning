import streamlit as st # pip install streamlit

radio = st.radio("Do you want a drink?", ("yes", "sure!"))

if radio == "yes":
    st.write("This is for you!")
else:
    st.write("perfect!")
    