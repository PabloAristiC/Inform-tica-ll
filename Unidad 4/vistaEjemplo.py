import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5.uic import loadUi;

class Ventana(QMainWindow):
    def __init__(self): #Constructor de la clase
        #Inicializa la ventana
        QMainWindow.__init__(self)
        loadUi(r"VentanaPrincipal.ui",self) #Lee el archivo de QtDesigner
        self.setWindowTitle("Ventana Principal") #Añadimos un título a nuestra ventana
        self.setup()
        #Conectar botón a función
    def setup(self):
        self.pushButton.clicked.connect(self.funcion) #cuando el botón se presiona, se ejecutará el método funcion().
    def funcion(self):
        self.ventanaSecundaria=ventanaSecundaria() #Asociación entre las ventanas
        self.ventanaSecundaria.show()
class ventanaSecundaria(QDialog):
    def __init__(self): #Constructor de la clase
        #Inicializa la ventana
        QDialog.__init__(self)
        loadUi(r"ventanaEmergente.ui",self) #Lee la ventana emergente
        self.setWindowTitle("Ventana Secundaria") #Añadimos un título a nuestra ventana
        self.setup()
    def setup(self):
        self.boton.accepted.connect(self.funcion)
        self.boton.rejected.connect(lambda:self.close())
    def funcion(self):
        pass
app = QApplication(sys.argv)
# se crea la instancia de la ventana
miVentana = Ventana()
# se muestra la ventana 
miVentana.show()
# se entrega el control al sistema operativo
sys.exit(app.exec_())