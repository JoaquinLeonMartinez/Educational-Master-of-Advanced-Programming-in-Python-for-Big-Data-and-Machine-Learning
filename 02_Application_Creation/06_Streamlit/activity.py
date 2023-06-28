'''
    Author: Joaquin Leon Martinez
'''
import streamlit as st # pip install streamlit
import quandl
import pandas as pd
import plotly.express as px
import pickle
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Title
st.title("Activity 13: Joaquín León Martínez")

# Companies
companies = ("GOOGL","AAPL", "TSLA", "MSFT", "NFLX")
columns = ("Open","High", "Low", "Close", "Volume")

# Select the company
option = st.selectbox("Select one: ", companies)
st.write("You choose:", option)

# from 1 to 5 years
years = st.slider("Select how many years do you want to plot: ",
                  1, 5, 1)
st.write("You choose: ", years)
final_year = 2014 + years

# Filter
column = st.selectbox("Filter by: ", columns)
st.write("You choose:", option)

# Get the data from quandl
data = quandl.get(f"WIKI/{option}", 
                  start_date = "2015-1-1", 
                  end_date=f"{final_year}-12-31")

# Apply the filter
st.write("Data before filter:")
st.write(data)
st.write("Data after filter:")
data = data[[column]]
st.write(data)

# Plot the graphs
st.write("Graph selected:")
st.line_chart(data)

# Iris dataset:
st.title("IRIS DATASET")

# Prediction code
filename = 'iris_model.sav'

sepalLengthCm = st.number_input("Introduce Sepal Length: ")
sepalWidthCm = st.number_input("Introduce Sepal Width: ")
petalLengthCm = st.number_input("Introduce Petal Length: ")
petalWidthCm = st.number_input("Introduce Petal Width: ")

def make_prediction(valueSepalLength, valueSepalWidth, valuePepalLength, valuePepalWidth):
    loaded_model = pickle.load(open(filename, 'rb'))
    entryData = [[float(valueSepalLength), float(valueSepalWidth), float(valuePepalLength), float(valuePepalWidth)]]
    prediction = loaded_model.predict(entryData)
    prediction = ''.join(prediction)
    return prediction

if st.button("prediction"):
    prediction = make_prediction(sepalLengthCm, sepalWidthCm, petalLengthCm, petalWidthCm)
    st.write("Prediction: ", prediction)
    
# Plot
df = px.data.iris()
st.write(df)
columnsIris = ("sepal_length","sepal_width", "petal_length", "petal_width", "species")
filter = st.selectbox("Filter by: ", columnsIris)
st.write("You choose:", filter)
df = df[[filter]]
st.write(df)
st.line_chart(df)