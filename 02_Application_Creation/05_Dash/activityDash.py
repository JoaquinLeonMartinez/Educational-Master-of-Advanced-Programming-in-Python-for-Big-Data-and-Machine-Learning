'''
Author: Joaquin Leon Martinez

Nota: el modelo esta en el .zip, 
si prefieres generarlo desde la app 
puedes pulsar el boton de generar 
(como en las actividades que entregue anteriormente)

Dudas: 

1 - Para los calbacks no he logrado hacer que el button
no tenga que pasarle ningun dato (me pide al menos el n_clicks para que funcione)
¿como se puede hacer para que el input sea un button y que no envie ningun dato?

Si me puedes responder las dudas en los comentarios de la actividad te lo agradeceria! 
'''

import dash
from dash import dcc
from dash import html
import plotly.express as px
from dash.dependencies import Input, Output, State
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle
import quandl
import yfinance as yf

filename = 'iris_model.sav'

app = dash.Dash()

# Plots Codes
df = px.data.iris()
figure1 = px.scatter(df, x="sepal_length", y="sepal_width", color="species")
df2 = quandl.get("FRED/GDP", start_date="2001-12-31", end_date="2005-12-31")
figure2= px.line(df2, title="GDP PIB MARKET QUOTE 2001-2005 (quandl)")
df3 = yf.download("AMZN", start="2017-01-01", end="2017-12-31")
figure3= px.line(df3, title="AMAZON STOCK MARKET QUOTE 2017 (yfinance)")

# Output & Input code
app.layout = html.Div([   
    html.Label('Sepal length: '),
    html.Div(dcc.Input(id="inputSepalLength", value="1", type="text")),
    html.Br(),
    html.Label('Sepal width:   '),
    html.Div(dcc.Input(id="inputSepalWidth", value="1", type="text")),
    html.Br(),
    html.Label('Pepal length: '),
    html.Div(dcc.Input(id="inputPepalLength", value="1", type="text")),
    html.Br(),
    html.Label('Pepal width:   '),
    html.Div(dcc.Input(id="inputPepalWidth", value="1", type="text")),
    html.Br(),
    html.Br(),
    html.Button('Train', id='trainButton', n_clicks=0),
    html.Div(id='train_output', children='Not trained'),
    html.Br(),    
    html.Button('Make prediction', id='predictionButton', n_clicks=0),
    html.Div(id='prediction_output', children='Waiting'),
    html.H1(children="Iris Sepal graph (length-width)"),
    dcc.Graph(figure=figure1),  
    html.H1(children="DASH APP TO STOCK MARKETS (quandl)"),
    dcc.Graph(figure=figure2),
    html.H1(children="DASH APP TO STOCK MARKETS (yfinance)"),
    dcc.Graph(figure=figure3)  
])


@app.callback(
    Output('train_output', 'children'),
    Input('trainButton', 'n_clicks')
)
def train_button(n_clicks):
    exit = 'Not trained'
    if(n_clicks > 0):
        train_and_save_model()
        exit = 'Trained'
    return exit

@app.callback(
    Output('prediction_output', 'children'),
    Input('predictionButton', 'n_clicks'),
    State('inputSepalLength', 'value'),
    State('inputSepalWidth', 'value'),
    State('inputPepalLength', 'value'),
    State('inputPepalWidth', 'value')
)
def prediction_button(n_clicks, valueSepalLength, valueSepalWidth, valuePepalLength, valuePepalWidth):
    exit = 'Waiting'
    if(n_clicks > 0):
        exit = make_prediction(valueSepalLength, valueSepalWidth, valuePepalLength, valuePepalWidth)
    
    return exit
    
def train_and_save_model():
    df = px.data.iris()
    X = df.drop(["species", "species_id"], axis = 1)
    Y = df["species"]
    clf = DecisionTreeClassifier()
    clf.fit(X, Y)
    pickle.dump(clf, open(filename, 'wb'))

def make_prediction(valueSepalLength, valueSepalWidth, valuePepalLength, valuePepalWidth):
    loaded_model = pickle.load(open(filename, 'rb'))
    entryData = [[float(valueSepalLength), float(valueSepalWidth), float(valuePepalLength), float(valuePepalWidth)]]
    prediction = loaded_model.predict(entryData)
    prediction = ''.join(prediction)
    return prediction




if __name__ == "__main__":
    app.run_server(debug=True)


