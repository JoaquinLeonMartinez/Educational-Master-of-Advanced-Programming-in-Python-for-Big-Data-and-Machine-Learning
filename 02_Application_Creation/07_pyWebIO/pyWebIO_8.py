from pywebio.input import * # pip install pywebio
from pywebio.output import *
import pywebio

def click_function(button_value):
      if button_value == "Java" or button_value == "C++":
            put_text(button_value, ": It is a good programming language")
      else:
            put_text(button_value, ": it is amazing!")

put_buttons(["Java","C++","Python"], onclick=click_function)
            
pywebio.session.hold() # keep the session active
