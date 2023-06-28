from PyQt5.QtWidgets import *
#from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

app = QApplication(sys.argv)

ventana = QMainWindow()

ventana. setGeometry (800,100, 500,500)
ventana. setWindowTitle("Mi primera Aplicacién PyQt")

label_1 = QLabel(ventana)
label_1.setText("Aplicacién programada con PyQt5")
label_1.adjustSize()
label_1.move(150, 26)

label_2 = QLabel(ventana)
label_2.setText("Escribe algo en el siguiente QLineEdit:")
label_2.adjustSize()
label_2.move(20, 100)

def imprimir():
    print(line_edit_1.text())
    
def salir():
    ventana.close()

boton_1 = QPushButton(ventana)
boton_1.setText("Imprimir en cmd")
boton_1.clicked.connect(imprimir)
boton_1.move(20,200)

boton_2 = QPushButton(ventana)
boton_2.setText("Salir")
boton_2.clicked.connect(salir)
boton_2.move(390,450) 

line_edit_1 = QLineEdit(ventana)
line_edit_1.move(20, 150)

ventana.show()
sys.exit(app.exec_())   


