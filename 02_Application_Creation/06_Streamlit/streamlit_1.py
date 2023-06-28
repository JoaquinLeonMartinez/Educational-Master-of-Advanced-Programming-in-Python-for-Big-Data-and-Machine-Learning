import pandas as pd
import streamlit as st # pip install streamlit

st.title("Firs Streamlit app")
st.write("Example of text")

st.write("We are going to write a df below")
df = pd.DataFrame({"a":[10, 20, 30, 20], "b": [40, 15, 36, 80]})
st.write(df)
st.write("Bars plot: ")
st.bar_chart(df)

# to run the script: streamlit run streamlit_1.py  