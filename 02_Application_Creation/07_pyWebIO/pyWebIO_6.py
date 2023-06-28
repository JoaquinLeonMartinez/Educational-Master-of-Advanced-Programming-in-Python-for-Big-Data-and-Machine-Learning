from pywebio.input import * # pip install pywebio
from pywebio.output import *

popup("Pop up title",
      [
            put_html("<h1> Example htmpl H1</h1>"),
            put_html("<h2> Example htmpl H2</h2>"),
            put_html("<h3> Example htmpl H3</h3>")
      ])

