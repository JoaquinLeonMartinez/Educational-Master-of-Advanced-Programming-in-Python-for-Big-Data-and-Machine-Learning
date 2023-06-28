import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import pandas as pd

window = tk.Tk()

window.title("Embedding in TK")

df = pd.DataFrame({"x": [0,1,2,3,4], "y": [10,15,5,25,30]})

figure = Figure(figsize=(6,4))
figure.add_subplot(111).plot(df.y)

canvas = FigureCanvasTkAgg(figure, window)
canvas.draw()
canvas.get_tk_widget().pack()

toolbar = NavigationToolbar2Tk(canvas, window)
toolbar.update()
canvas.get_tk_widget().pack()

window.mainloop()