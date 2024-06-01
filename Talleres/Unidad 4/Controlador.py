from Vista import Ventana
import sys
from PyQt5.QtWidgets import QApplication
from Modelo import Modelo

class Controlador(object):
    def __init__(self, modelo):
        self.__mi_modelo = modelo
    def registrar_usuario(self, nombre,apellido,edad,id):
        return self.__mi_modelo.registrarUsuario(nombre,apellido,edad,id)
    def validar_administrador(self, u, p): 
        return self.__mi_modelo.verificarAdministrador(u,p) 

class Principal(object):
    def __init__(self):
        self.__app = QApplication(sys.argv)
        self.__mi_vista = Ventana()
        self.__mi_modelo = Modelo()
        self.__mi_controlador = Controlador(self.__mi_modelo)
        self.__mi_vista.asignarControlador(self.__mi_controlador) 
    def main(self):
        self.__mi_vista.show()
        sys.exit(self.__app.exec_())   

p = Principal()
p.main()