import streamlit as st # pip install streamlit
from datetime import time

# slider example 1
languages = st.slider("How many languages do you know?", 0, 15, 1)
st.write("You selected: ", languages)

# slider example 2
range = st.slider("Select a values range", 0.0, 100.0, (25.0, 75.0))
st.write("You selected: ", range)

# slider example 3 
time = st.slider("Meeting time: ",
                 value = (time(13, 30), time(15, 30)))
st.write("Your meeting is at: ", time)