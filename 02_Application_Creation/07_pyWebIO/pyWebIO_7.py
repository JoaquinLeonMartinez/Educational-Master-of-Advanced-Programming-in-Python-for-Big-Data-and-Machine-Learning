from pywebio.input import * # pip install pywebio
from pywebio.output import *

# menu

with put_collapse("Open menu with 4 options"):
      for i in range(1,5, 1):
            put_text("Opcion: ", i)
