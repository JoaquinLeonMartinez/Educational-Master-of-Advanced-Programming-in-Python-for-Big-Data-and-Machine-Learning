from pywebio.input import * # pip install pywebio
from pywebio.output import *

put_row([
      put_column([
            put_code("Row 1, Column 1"), None,
            put_row([
                  put_code("Row added 2, text 1"), None,
                  put_code("Row added 2, text 2"), None,
                  put_code("Row added 2, text 3")
                  
            ])        
                       
      ])
])

put_row([
      put_column([
            put_code("Row 3, Column 1"), None,
            put_row([
                  put_code("Row added 4, text 1"), None,
                  put_code("Row added 4, text 2"), None,
                  put_code("Row added 4, text 3") 
            ])                  
      ])
])

