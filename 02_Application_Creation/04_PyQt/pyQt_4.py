from PyQt5.QtWidgets import *

# Creacion de la ventana con POO
class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)


if __name__=="__main__":
    app = QApplication([])
    ventana = Window()
    ventana.show()
    app.exec_()