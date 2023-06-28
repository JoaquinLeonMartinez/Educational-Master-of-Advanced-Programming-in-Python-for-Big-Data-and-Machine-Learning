from pywebio.input import * # pip install pywebio
from pywebio.output import *

# radio
radio("Select one framework", 
      options=["PyQt", "TKinter"])

# checkbox
checkbox("Do you know Dash framework?",
      options=["yes", "no"])

# select
select("Select a framework <select> :",
      options=["Django", "Streamlit"])

