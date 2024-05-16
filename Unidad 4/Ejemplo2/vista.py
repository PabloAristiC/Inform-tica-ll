#importamos las librerías necesarias
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi;

'''
QMainWindow: Es una clase que proporciona una ventana principal para aplicaciones GUI.

loadUi: Esta función permite cargar un archivo .ui creado con Qt Designer. 
El archivo .ui define la estructura y diseño de la interfaz gráfica.
'''

#Creamos una clase ventana, que se hereda de la clase "QMainWindow"
class Ventana(QMainWindow):
    def __init__(self): #Constructor de la clase
        #Inicializa la ventana
        QMainWindow.__init__(self)
        loadUi(r"C:\Users\Pablo\Informática ll\git.repositorio\Inform-tica-ll\Unidad 4\pruebaVista.ui",self) #Lee el archivo de QtDesigner
        self.setWindowTitle("Ejemplo") #Añadimos un título a nuestra ventana
        #Conectar botón a función
        self.Boton.clicked.connect(self.funcion) #cuando el botón se presiona, se ejecutará el método funcion().
        self.Salir.clicked.connect(lambda:self.close())#Función predeterminada para salir
    def funcion(self):
        self.label.setText('Ah no chao')


# se crea la instancia de la aplicación
app = QApplication(sys.argv)
# se crea la instancia de la ventana
miVentana = Ventana()
# se muestra la ventana 
miVentana.show()
# se entrega el control al sistema operativo
sys.exit(app.exec_())