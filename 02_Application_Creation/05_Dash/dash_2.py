# pip install dash
import dash
from dash import html

# We create our app:
app = dash.Dash()
app.layout = html.Div("My first Dash App")

if __name__ == "__main__":
    app.run_server(debug=True)

