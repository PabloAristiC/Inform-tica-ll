# Importar librerias básicas
from PyQt5.QtGui import QIntValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp
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
        loadUi(r'C:\Users\Pablo\Informática ll\git.repositorio\Inform-tica-ll\Unidad 4\Ejemplo_login\VentanaLogin.ui',self)
        self.setup()#Siempre hay que llamarla
    def setup(self): # Llama al método setup, que está definido más adelante en la clase.
        #se programa la senal para el boton
        self.campo_usuario.setValidator(QRegExpValidator(QRegExp(r"[a-zA-Z]+")))
        self.campo_password.setValidator(QRegExpValidator(QRegExp(r"[0-9]+")))
        self.boton_ingresar.clicked.connect(self.accion_ingresar) #cuando el botón se presiona, se ejecutará el método accion_ingresar.
        self.boton_registrar.clicked.connect(self.accion_registrar)
    def accion_registrar(self):
        self.ventanaSecundaria=ventanaSecundaria(self) #Asociación entre las ventanas, siempre poner el self!!!!!!!!
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
    def recibir_info(self,u,p):
        resultado=self.__controlador.validar_usuario(u,p)
        msg = QMessageBox(self)
        msg.setWindowTitle("Resultado")
        if resultado==True:
            msg.setText("Error, usuario ya existente")
        else:
            if u=='':
                msg.setText("Error, usuario vacío")
            elif p=='':
                msg.setText("Error, contraseña vacía")
            else:
                self.__controlador.registrar_usuario(u,p)
                msg.setText("Usuario registrado exitosamente")   
        msg.show()    
class ventanaSecundaria(QDialog):
    def __init__(self,ppal=None): #Constructor de la clase
        #Inicializa la ventana
        QDialog.__init__(self,ppal)
        loadUi(r"C:\Users\Pablo\Informática ll\git.repositorio\Inform-tica-ll\Unidad 4\Ejemplo_login\registrar.ui",self) #Lee la ventana emergente
        self.setWindowTitle("Ventana Secundaria") #Añadimos un título a nuestra ventana
        self.parent=ppal
        self.setup()
    def setup(self):
        self.usuario.setValidator(QRegExpValidator(QRegExp(r"[a-zA-Z]+")))
        self.contrasena1.setValidator(QRegExpValidator(QRegExp(r"[0-9]+")))
        self.boton.accepted.connect(self.conectarRegistro)
        self.boton.rejected.connect(lambda:self.close())
    def conectarRegistro(self):
        usuario=self.usuario.text()
        contraseña=self.contrasena1.text()
        self.parent.recibir_info(usuario,contraseña)
        self.close()