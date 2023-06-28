from PyQt5.QtWidgets import *

class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(500, 400)
        # Label
        self.label = QLabel(self)
        self.label.setGeometry(30,30,140,50)
        self.label.setText("Label en POO")
        self.label.setStyleSheet("background-color: blue; color: white; margin: 2px; font-size: 20px;")
        self.label.setObjectName("label_1")
        # Button
        self.button = QPushButton(self)
        self.button.setGeometry(30,100,120,50)
        self.button.setText("Button en POO")
        self.button.setStyleSheet("background-color: grey; color: black; margin: 2px; font-size: 15px;")
        self.button.setObjectName("button_1")
        # Line Edit
        self.line_edit = QLineEdit(self)
        self.line_edit.setGeometry(30, 170, 140, 30)
        self.line_edit.setStyleSheet("border: 2px solid #3232C0;")
        self.line_edit.setObjectName("line_edit_1")
        
if __name__=="__main__":
    app = QApplication([])
    ventana = Window()
    ventana.show()
    app.exec_()
