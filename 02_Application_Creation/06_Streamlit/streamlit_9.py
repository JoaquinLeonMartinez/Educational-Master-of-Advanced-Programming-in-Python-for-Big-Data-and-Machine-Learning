import streamlit as st # pip install streamlit
import quandl

# Title
st.title("Streamplit finance graph")

# Companies
companies = ("GOOGL","AAPL", "TSLA", "MSFT", "NFLX")

# Select the company
option = st.selectbox("Select one: ", companies)

st.write("You choose:", option)

# from 1 to 5 years
years = st.slider("Select how many years do you want to plot: ",
                  1, 5, 1)
st.write("You choose: ", years)
final_year = 2014 + years

# Get the data from quandl
data = quandl.get(f"WIKI/{option}", 
                  start_date = "2015-1-1", 
                  end_date=f"{final_year}-12-31")

# Head
st.write("Head")
st.write(data.head())

# Tail
st.write("Tail")
st.write(data.tail())

# We onli¡y need "Close" column
data = data[["Close"]]
st.write("Close column:")
st.write(data)

# Plot the graphs
st.write("Graph selected:")
st.line_chart(data)