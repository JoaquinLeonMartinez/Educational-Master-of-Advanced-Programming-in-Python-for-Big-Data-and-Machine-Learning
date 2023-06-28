# pip install plotly-express
import plotly.express as px

df = px.data.iris()
X = df.drop(["species", "species_id"], axis = 1)
print(X)