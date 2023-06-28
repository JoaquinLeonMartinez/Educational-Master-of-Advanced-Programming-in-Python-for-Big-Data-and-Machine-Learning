from PyQt5.QtWidgets import *
import sys

if __name__=="__main__":
    app = QApplication(sys.argv)
    ventana = QMainWindow()
    ventana.setGeometry(800,100,500,500)
    ventana.setWindowTitle("Aplicacion con varios elementos")
    ventana.setStyleSheet("background-color: grey;")
    
    # Buttons
    button_1 = QPushButton('boton 1', ventana)
    button_1.move(100,100)
    button_2 = QPushButton('boton 2', ventana)
    button_2.move(100,200)
    button_3 = QPushButton('boton 3', ventana)
    button_3.setStyleSheet("background-color: grey; color: black;")
    button_3.move(100,300)
    
    estilos="""QPushButton{
        background-color: grey;
        padding: 2px;
    }"""

    QApplication.instance().setStyleSheet(estilos)
    ventana.show()
    sys.exit(app.exec_())

        


