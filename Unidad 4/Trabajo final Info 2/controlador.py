import sys
from PyQt5.QtWidgets import QApplication
from modelo import SistemaGestionModelo
from Vista import *

class Coordinador:
    def __init__(self, vista, modelo):
        self.vista = vista
        self.modelo = modelo
    def agregarDoctor(self,usuario, contrasena):
        return self.modelo.agregar_doctor(usuario,contrasena)
    def ValidarDoctor(self,usuario,contrasena):
        return self.modelo.validarDoctor(usuario,contrasena)
    def agregarPaciente(self,nombre,apellido,edad,id,fecha):
        return self.modelo.agregar_paciente(nombre,apellido,edad,id,fecha)
    def cargarDiagnostico(self,fs,fp,fqrs,inicio,fin):
        return self.modelo.diagnosticar_paciente(fs,fp,fqrs,inicio,fin)

class Controlador:
    def __init__(self):
        self.modelo = SistemaGestionModelo()
        self.app = QApplication(sys.argv)
        self.ventanaPrincipal = VentanaPrincipal()
        self.coordinador = Coordinador(self.ventanaPrincipal, self.modelo)
        self.ventanaPrincipal.asignarControlador(self.coordinador)

    def iniciar(self):
        self.ventanaPrincipal.show()
        sys.exit(self.app.exec_())

controlador=Controlador()
controlador.iniciar()