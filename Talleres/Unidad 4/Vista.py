from PyQt5.QtGui import QIntValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDialog
from PyQt5.uic import loadUi;

class Ventana(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi(r'C:\Users\Pablo\Informática ll\git.repositorio\Inform-tica-ll\Talleres\Unidad 4\VentanaLogin.ui',self)
        self.ventanaUsuarios=ventanaUsuarios(self)
        self.setup()
    def setup(self):
        self.campo_usuario.setValidator(QRegExpValidator(QRegExp(r"[\w]+")))
        self.campo_password.setValidator(QRegExpValidator(QRegExp(r"[\w]+")))
        self.boton_ingresar.clicked.connect(self.accion_ingresar)
    def asignarControlador(self,c):
        self.__controlador = c
    def accion_ingresar(self):
        usuario = self.campo_usuario.text()
        password = self.campo_password.text()
        resultado = self.__controlador.validar_administrador(usuario,password) 
        msg = QMessageBox(self)
        msg.setWindowTitle("Resultado")
        if resultado == True:
            self.ventanaUsuarios.show()
            self.hide()
        else:
            msg.setText("Administrador Inválido")
            msg.show()
    def recibir_info(self,nombre,apellido,edad,id):
        msg = QMessageBox(self)
        msg.setWindowTitle("Resultado")
        if nombre=='':
            msg.setText("Error, usuario vacío")
            msg.show()
            self.show()
        elif apellido=='':
            msg.setText("Error, contraseña vacía")
            msg.show()
            self.show()
        elif edad=='':
            msg.setText("Error, edad vacía")
            msg.show()
            self.show()
        elif id=='':
            msg.setText("Error, identificación vacía")
            msg.show()
            self.show()
        else:
            if self.__controlador.registrar_usuario(nombre,apellido,edad,id)==False:
                msg.setText("Usuario registrado exitosamente") 
                msg.show()
                self.show()
            else:
                msg.setText("Error, ID ya registrado")
                msg.show()
                self.show()

class ventanaUsuarios(QDialog):
    def __init__(self,ppal=None):
        QDialog.__init__(self,ppal)
        loadUi(r'C:\Users\Pablo\Informática ll\git.repositorio\Inform-tica-ll\Talleres\Unidad 4\Usuarios.ui',self)
        self.setWindowTitle("Ventana Usuarios")
        self.parent=ppal
        self.setup()
    def setup(self):
        self.Nombre.setValidator(QRegExpValidator(QRegExp(r"[a-zA-Z]+")))
        self.Apellido.setValidator(QRegExpValidator(QRegExp(r"[a-zA-Z]+")))
        self.Edad.setValidator(QRegExpValidator(QRegExp(r"[0-9]+")))
        self.ID.setValidator(QRegExpValidator(QRegExp(r"[0-9]+")))
        self.buttonBox.accepted.connect(self.conectarRegistro)
        self.buttonBox.rejected.connect(self.accionCerrar)
    def accionCerrar(self):
        self.parent.show()
        self.close()
    def conectarRegistro(self):
        Nombre=self.Nombre.text()
        Apellido=self.Apellido.text()
        Edad=self.Edad.text()
        ID=self.ID.text()
        self.parent.recibir_info(Nombre,Apellido,Edad,ID)
        self.close()
