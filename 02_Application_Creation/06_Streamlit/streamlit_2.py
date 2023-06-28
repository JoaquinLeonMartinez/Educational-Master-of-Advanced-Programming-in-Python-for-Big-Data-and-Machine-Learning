import streamlit as st # pip install streamlit

def suma(a,b):
    return a+b

st.text('5 + 10 = ') # text y write are similar

if st.button("suma"):
    result = suma(5,10)
    st.write("Result: ", result)

# to run the script: streamlit run streamlit_2.py  