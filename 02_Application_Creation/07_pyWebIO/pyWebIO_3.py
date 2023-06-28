from pywebio.input import * # pip install pywebio
from pywebio.output import *

# textarea
textarea("Text area", rows=3, 
         placeholder="Write here!")

# textarea (with editable code)
textarea("Code Edit",
         code={"mode": "python",
               "theme": "dracula"},
         value = "import pandas as pd\n #Write here your Python code"
         )