from pywebio.input import * # pip install pywebio
from pywebio.output import *

style(put_text("Blue text"), "color: blue")

put_table([
      [style(put_text("Blue text"), "color: blue"),
      style(put_text("Red text"), "color: red")],
      
      [style(put_text("Orange text"), "color: orange"),
      style(put_text("Green text"), "color: green")]
])
