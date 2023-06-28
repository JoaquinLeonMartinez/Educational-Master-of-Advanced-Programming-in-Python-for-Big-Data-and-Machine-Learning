from pywebio.input import * # pip install pywebio
from pywebio.output import *

# text output
put_text("With put_text we can output text")

put_table([["Company", "Quote"],
          ["X", "10"],
          ["Y", "30"],
          ["Z", "20"]])

put_markdown("--Example (strike)--")
put_markdown("**Example (bold)**")
put_markdown("*Example (cursive)*")