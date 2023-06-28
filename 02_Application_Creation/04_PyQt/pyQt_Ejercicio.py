
'''
Author: Joaquin Leon Martinez
'''
from PyQt5.QtWidgets import *
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import pickle

filename = 'iris_model.sav'

def trainModel():
    df = pd.read_csv("iris_dataset.csv")
    X = df.drop(["Species"], axis = 1)
    Y = df["Species"]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state = 0)
    clf = DecisionTreeClassifier()
    clf.fit(X_train, Y_train)
    pickle.dump(clf, open(filename, 'wb'))

def makePrediction():
    loaded_model = pickle.load(open(filename, 'rb'))
    entryData = [[float(line_edit_1.text()), float(line_edit_2.text()), float(line_edit_3.text()), float(line_edit_4.text())]]
    prediction = loaded_model.predict(entryData)
    prediction = ''.join(prediction)
    label_5.setText(prediction)

def drawPlot(plotVariable):
    df = pd.read_csv("iris_dataset.csv")
    ax.clear()
    ax.plot(df[plotVariable])
    canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = QMainWindow()
    ventana.setGeometry (800, 100, 700,700)
    ventana.setWindowTitle("Ejercicio Joaquin Leon Martinez")

    label_1 = QLabel(ventana)
    label_1.setText("Sepal Length (cm)")
    label_1.adjustSize()
    label_1.move(20, 320)

    label_2 = QLabel(ventana)
    label_2.setText("Sepal Width (cm)")
    label_2.adjustSize()
    label_2.move(20, 360)
    
    label_3 = QLabel(ventana)
    label_3.setText("Petal Length (cm)")
    label_3.adjustSize()
    label_3.move(20, 400)
    
    label_4 = QLabel(ventana)
    label_4.setText("Petal Width (cm)")
    label_4.adjustSize()
    label_4.move(20, 440)
    
    line_edit_1 = QLineEdit(ventana)
    line_edit_1.move(200, 320)

    line_edit_2 = QLineEdit(ventana)
    line_edit_2.move(200, 360)
   
    line_edit_3 = QLineEdit(ventana)
    line_edit_3.move(200, 400)
    
    line_edit_4 = QLineEdit(ventana)
    line_edit_4.move(200, 440)

    boton_1 = QPushButton(ventana)
    boton_1.setText("Train Model")
    boton_1.clicked.connect(trainModel)
    boton_1.move(20,500)
    
    boton_2 = QPushButton(ventana)
    boton_2.setText("Prediction")
    boton_2.clicked.connect(makePrediction)
    boton_2.move(200,500)
    
    label_5 = QLabel(ventana)
    label_5.setText("Prediction")
    label_5.adjustSize()
    label_5.move(350, 510)
    
    # Plot code
    figure = Figure()
    canvas = FigureCanvas(figure)
    canvas.setFixedSize(200, 200)
    
    layout = QVBoxLayout()
    layout.addWidget(canvas)
 
    widget = QWidget()
    widget.setLayout(layout)
    
    widget.setFixedSize(200, 200)
    ventana.setCentralWidget(widget)
    
    ax = figure.add_subplot(111)
    
    boton_3 = QPushButton(ventana)
    boton_3.setText("Sepal Length")
    boton_3.clicked.connect(lambda: drawPlot("SepalLengthCm"))
    boton_3.move(250,20)
    
    boton_4 = QPushButton(ventana)
    boton_4.setText("Sepal Width")
    boton_4.clicked.connect(lambda: drawPlot("SepalWidthCm"))
    boton_4.move(250,70)
    
    boton_5 = QPushButton(ventana)
    boton_5.setText("Petal Length")
    boton_5.clicked.connect(lambda: drawPlot("PetalLengthCm"))
    boton_5.move(250,120)
    
    boton_6 = QPushButton(ventana)
    boton_6.setText("Petal Width")
    boton_6.clicked.connect(lambda: drawPlot("PetalWidthCm"))
    boton_6.move(250,170)   
    
    ventana.show()
    sys.exit(app.exec_())   


