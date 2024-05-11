
# Importar librerias básicas
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDialog
from PyQt5.uic import loadUi;

'''
QMainWindow: Es una clase que proporciona una ventana principal para aplicaciones GUI.

loadUi: Esta función permite cargar un archivo .ui creado con Qt Designer. 
El archivo .ui define la estructura y diseño de la interfaz gráfica.

QMessageBox: Es una clase que proporciona un cuadro de diálogo para mostrar mensajes.
'''

class Ventana(QMainWindow):
    def __init__(self): #Constructor de la clase
        QMainWindow.__init__(self)#Siempre hay que llamarla
        loadUi(r'Ejemplo_login\VentanaLogin.ui',self)
        self.setup()#Siempre hay que llamarla
    def setup(self): # Llama al método setup, que está definido más adelante en la clase.
        #se programa la senal para el boton
        self.boton_ingresar.clicked.connect(self.accion_ingresar) #cuando el botón se presiona, se ejecutará el método accion_ingresar.
        self.boton_registrar.clicked.connect(self.funcion)
    def funcion(self):
        self.ventanaSecundaria=ventanaSecundaria() #Asociación entre las ventanas
        self.ventanaSecundaria.show()
    def asignarControlador(self,c): #Guarda un controlador para posteriormente hacer validaciones
        self.__controlador = c
    def accion_ingresar(self):
        #Extraer el texto de los campos campo_usuario y campo_password.
        usuario = self.campo_usuario.text()
        password = self.campo_password.text()
        #esta informacion la debemos pasar al controlador
        resultado = self.__controlador.validar_usuario(usuario,password) #Función de validación del controlador
        #Se crea la ventana de resultado
        msg = QMessageBox(self)
        msg.setWindowTitle("Resultado")
        #se selecciona el resultado de acuerdo al resultado de la operacion
        if resultado == True:
            msg.setText("Usuario Válido")
        else:
            msg.setText("Usuario Inválido")
        #se muestra la ventana
        msg.show()   
class ventanaSecundaria(QDialog):
    def __init__(self): #Constructor de la clase
        #Inicializa la ventana
        QDialog.__init__(self)
        loadUi(r"Ejemplo_login\registrar.ui",self) #Lee la ventana emergente
        self.setWindowTitle("Ventana Secundaria") #Añadimos un título a nuestra ventana
        self.setup()
    def setup(self):
        self.boton.accepted.connect(self.funcion)
        self.boton.rejected.connect(lambda:self.close())
    def funcion(self):
        usuario=self.usuario.text()
        pass