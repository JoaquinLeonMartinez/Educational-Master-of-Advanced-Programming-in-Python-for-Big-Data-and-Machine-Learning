'''
Author: Joaquin Leon Martinez

Notes: Me disculpo de antemano por lo feo que ha quedado

'''

import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import pickle

filename = 'iris_model.sav'
window = tk.Tk()

window.title("First Tkinter app")
window.resizable(0,0)
window.geometry("600x600")
window.config(bg="white")

# Data prediction code:

def train_model():
    df = pd.read_csv("iris_dataset.csv")
    X = df.drop(["Species"], axis = 1)
    Y = df["Species"]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state = 0)
    clf = DecisionTreeClassifier()
    clf.fit(X_train, Y_train)
    pickle.dump(clf, open(filename, 'wb'))

def prediction():
    loaded_model = pickle.load(open(filename, 'rb'))
    entryData = [[e1.get(), e2.get(), e3.get(), e4.get()]]
    prediction = loaded_model.predict(entryData)
    prediction = ''.join(prediction)
    resultLabel = tk.Label(window, text=prediction).grid(row=8,column=1)

tk.Label(window, text="Enter the data related to the iris flower:").grid(row=1,column=0)
tk.Label(window, text="SepalLength (Cm)").grid(row=2,column=0)
tk.Label(window, text="SepalWidth (Cm)").grid(row=3,column=0)
tk.Label(window, text="PetalLength (Cm)").grid(row=4,column=0)
tk.Label(window, text="PetalWidth (Cm)").grid(row=5,column=0)
tk.Label(window, text="Prediction:").grid(row=8,column=0)


e1 = tk.Entry(window)
e1.insert(0, "")
e1.grid(row=2, column=1)

e2 = tk.Entry(window)
e2.insert(0, "")
e2.grid(row=3, column=1)

e3 = tk.Entry(window)
e3.insert(0, "")
e3.grid(row=4, column=1)

e4 = tk.Entry(window)
e4.insert(0, "")
e4.grid(row=5, column=1)

tk.Button(window, text="Train model",
          bg="red", fg="white", command=train_model).grid(row=7,column=0)

tk.Button(window, text="Predict",
          bg="red", fg="white", command=prediction).grid(row=7,column=1)

# We also print a plots with dataset data

def modifyPlot(plotVariable: str):
    plot.clear()
    plot.plot(df[plotVariable])
    
    canvas.draw()
    canvas.get_tk_widget().grid(row=14,column=1)

df = pd.read_csv("iris_dataset.csv")

figure = Figure(figsize=(3,2))
plot = figure.add_subplot(111)
plot.plot(df['SepalWidthCm'])

canvas = FigureCanvasTkAgg(figure, window)
canvas.draw()
canvas.get_tk_widget().grid(row=14,column=1)

tk.Button(window, text="Show Sepal Length",
          bg="red", fg="white", command=lambda:modifyPlot('SepalLengthCm')).grid(row=10,column=0)
tk.Button(window, text="Show Sepal Widht",
          bg="red", fg="white", command=lambda:modifyPlot('SepalWidthCm')).grid(row=11,column=0)
tk.Button(window, text="Show Petal Length",
          bg="red", fg="white", command=lambda:modifyPlot('PetalLengthCm')).grid(row=12,column=0)
tk.Button(window, text="Show Petal Width",
          bg="red", fg="white", command=lambda:modifyPlot('PetalWidthCm')).grid(row=13,column=0)

window.mainloop()