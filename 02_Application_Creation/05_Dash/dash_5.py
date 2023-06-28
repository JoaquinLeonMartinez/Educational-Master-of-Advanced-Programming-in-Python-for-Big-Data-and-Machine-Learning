import dash
from dash import dcc
from dash import html
import plotly.express as px
import quandl

df = quandl.get("WIKI/GOOGL.4", start_date="2015-01-01", end_date="2018-12-31")

figure1= px.line(df, title="GOOGLE STOCK MARKET QUOTE 2015-2018")

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children="DASH APP TO STOCK MARKETS"),
    dcc.Graph(figure=figure1)    
])


if __name__ == "__main__":
    app.run_server(debug=True)
