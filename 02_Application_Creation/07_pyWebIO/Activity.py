'''
    Author: Joaquin Leon Martinez
'''

from pywebio.input import * # pip install pywebio
from pywebio.output import *
import pickle
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

filename = 'iris_model.sav'

def make_prediction(valueSepalLength, valueSepalWidth, valuePepalLength, valuePepalWidth):
    loaded_model = pickle.load(open(filename, 'rb'))
    entryData = [[float(valueSepalLength), float(valueSepalWidth), float(valuePepalLength), float(valuePepalWidth)]]
    prediction = loaded_model.predict(entryData)
    prediction = ''.join(prediction)
    return prediction

sepal_length = input("Introduce the Sepal Length", type=NUMBER)
sepal_width =input("Introduce the Sepal Width", type=NUMBER)
petal_length =input("Introduce the Petal Length", type=NUMBER)
petal_width = input("Introduce the Petal Width", type=NUMBER)

prediction = make_prediction(sepal_length, sepal_width, petal_length, petal_width)

put_text("Prediction:", prediction)

put_text("Some other data:")

df = px.data.iris()

put_text(df.head())

df_sepal_length = df["sepal_length"]
df_sepal_width = df["sepal_width"]
df_petal_length = df["petal_length"]
df_petal_width = df["petal_width"]

figure1 = px.scatter(df_sepal_length, title="Sepal Length")
figure2 = px.scatter(df_sepal_width, title="Sepal Width")
figure3 = px.scatter(df_petal_length, title="Petal Length")
figure4 = px.scatter(df_petal_width, title="Petal Width")

put_row([
      put_column([
          put_html(figure1.to_html(include_plotlyjs="require", full_html=False)),
          put_html(figure2.to_html(include_plotlyjs="require", full_html=False))    
            ]),
      put_column([
          put_html(figure3.to_html(include_plotlyjs="require", full_html=False)),
          put_html(figure4.to_html(include_plotlyjs="require", full_html=False))         
            ])       
                       
      ])
