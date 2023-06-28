import dash
from dash import dcc
from dash import html
import plotly.express as px

df = px.data.iris()

figure1 = px.scatter(df, x="petal_length", y="petal_width", color="species")


app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children="Grafica del Iris Dataset para el petalo (Largo-Ancho)"),
    dcc.Graph(figure=figure1)    
])


if __name__ == "__main__":
    app.run_server(debug=True)

