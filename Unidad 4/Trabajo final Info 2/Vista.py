import numpy as np
from PyQt5 import QtCore
from PyQt5.QtCore import QRegExp
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDialog, QApplication
import sys
from PyQt5.QtGui import  QRegExpValidator
from PyQt5.uic import loadUi;

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi(r"ventana ppal (1).ui",self)
        self.setup()
    def setup(self):
        self.usuario.setValidator(QRegExpValidator(QRegExp(r"[a-zA-Z- ]+")))
        self.contrasena.setValidator(QRegExpValidator(QRegExp(r"[0-9]+")))
        self.ingresar.clicked.connect(self.ingresar1)
        self.paciente.clicked.connect(self.agregarPaciente)
        self.registrar.clicked.connect(self.registrar1)
        self.salir.clicked.connect(lambda:self.close())
        self.paciente.setEnabled(False)
    def ingresar1(self):
        usuario = self.usuario.text()
        contrasena = self.contrasena.text()
        msg = QMessageBox(self)
        msg.setWindowTitle("Resultado")
        if usuario=='':
            msg.setText('Error, Usuario Vacío')
        elif contrasena=='':
            msg.setText('Error, Contraseña Vacía')
        else:
            resultado = self.__controlador.ValidarDoctor(usuario, contrasena)
            if resultado == True:
                self.paciente.setEnabled(True)
                msg.setText('Usuario Válido')
            else:
                msg.setText("Usuario Incorrecto")
        msg.show()
    def registrar1(self):
        self.ventanaRegistro=ventanaRegistro(self)
        self.ventanaRegistro.show()
        self.hide()
    def agregarPaciente(self):
        self.ventanaUsuarios=ventanaUsuarios(self)
        self.ventanaUsuarios.show()
        self.hide()
    def asignarControlador(self,c):
        self.__controlador = c
    def recibirInfo(self,usuario,contrasena):
        msg = QMessageBox(self)
        msg.setWindowTitle("Resultado")
        if usuario=='':
            msg.setText('Error, Nombre Vacío')
        elif contrasena=='':
            msg.setText('Error, Contraseña Vacía')
        else:
            resultado = self.__controlador.agregarDoctor(usuario, contrasena)
            if resultado:
                msg.setText("El médico ya estaba registrado")
            else:
                msg.setText("Médico registrado con éxito")
        msg.show()
    def recibirPaciente(self,nombre,apellido,edad,id,fecha):
        resultado=self.__controlador.agregarPaciente(nombre,apellido,edad,id,fecha)
    def cargarDatos(self,fs,fp,fqrs,inicio,fin):
        self.ventanaEKG=VentanaEKG(self,fs,fp,fqrs,inicio,fin)
        self.ventanaEKG.show()
        self.ventanaDatos.hide()
    def pedirEKG(self):
        self.ventanaDatos=VentanaDatos(self)
        self.ventanaDatos.show()
    def recibirDatosSenal(self,senal_continua):
        self.__controlador.recibirDatosSenal(senal_continua)
    def graficar_datos(self,xmin,xmax):
        self.__controlador.devolverDatosSenal(xmin,xmax)
    def cargarDiagnostico(self,fs,fp,fqrs,inicio,fin):
        return self.__controlador.cargarDiagnostico(fs,fp,fqrs,inicio,fin)


class ventanaRegistro(QDialog):
    def __init__(self,ppal=None):
        QDialog.__init__(self,ppal)
        loadUi(r"Ventana_emergente (1).ui",self)
        self.setWindowTitle("Ventana Registro")
        self.parent=ppal
        self.setup()
    def setup(self):
        self.campo_usuario.setValidator(QRegExpValidator(QRegExp(r"[a-zA-Z- ]+")))
        self.campo_password.setValidator(QRegExpValidator(QRegExp(r"[0-9]+")))
        self.Registrarse.accepted.connect(self.registro)
        self.Registrarse.rejected.connect(self.salir)
    def salir(self):
        self.parent.show()
        self.close()
    def registro(self):
        usuario = self.campo_usuario.text()
        contrasena = self.campo_password.text()
        self.parent.recibirInfo(usuario, contrasena) 
        self.parent.show()
        self.close()

class ventanaUsuarios(QDialog):
    def __init__(self, ppal=None):
        QDialog.__init__(self,ppal)
        loadUi(r"Ventana 2.ui",self)
        self.setWindowTitle('Ventana Usuarios')
        self.parent=ppal
        self.setup()
    def setup(self):
        self.apellido.setValidator(QRegExpValidator(QRegExp(r"[a-zA-Z]+")))
        self.nombre.setValidator(QRegExpValidator(QRegExp(r"[a-zA-Z]+")))
        self.edad.setValidator(QRegExpValidator(QRegExp(r"[0-9]+")))
        self.id.setValidator(QRegExpValidator(QRegExp(r"[0-9]+")))
        self.fecha.setValidator(QRegExpValidator(QRegExp(r"[0-9]+/[0-9]+/[0-9]")))
        self.Registrarse.accepted.connect(self.registro)
        self.Registrarse.rejected.connect(self.salir)
        self.ekg.clicked.connect(self.cargarSenal)
        self.ekg.setEnabled(False)
    def salir(self):
        self.parent.show()
        self.close()
    def cargarSenal(self):
        self.parent.pedirEKG()
        self.hide()
    def registro(self):
        nombre=self.nombre.text()
        apellido=self.apellido.text()
        edad=self.edad.text()
        id=self.id.text()
        fecha=self.fecha.text()
        self.parent.recibirPaciente(nombre,apellido,edad,id,fecha)
        self.ekg.setEnabled(True)
        self.show()
    
class VentanaDatos(QDialog):
    def __init__(self,ppal=None):
        QDialog.__init__(self,ppal)
        loadUi(r"VentanaDatos.ui",self)
        self.setWindowTitle('Ventana Datos')
        self.parent=ppal
        self.setup()
    def setup(self):
        self.fs.setValidator(QRegExpValidator(QRegExp(r"[0-9]+")))
        self.fp.setValidator(QRegExpValidator(QRegExp(r"[0-9]+")))
        self.fqrs.setValidator(QRegExpValidator(QRegExp(r"[0-9-.]+")))
        self.inicio.setValidator(QRegExpValidator(QRegExp(r"[0-9]+")))
        self.fin.setValidator(QRegExpValidator(QRegExp(r"[0-9]+")))
        self.buttonBox.accepted.connect(self.datos)
        self.buttonBox.rejected.connect(lambda: self.close())
    def datos(self):
        fs=self.fs.text()
        fp=self.fp.text()
        fqrs=self.fqrs.text()
        inicio=self.inicio.text()
        fin=self.fin.text()
        self.parent.cargarDatos(fs,fp,fqrs,inicio,fin)

class VentanaEKG(QDialog):
    def __init__(self,ppal,fs,fp,fqrs,inicio,fin):
        QDialog.__init__(self,ppal)
        loadUi(r"Ventana 3.ui",self)
        self.fs=fs
        self.fp=fp
        self.fqrs=fqrs
        self.inicio=inicio
        self.fin=fin
        self.setWindowTitle('Ventana Estudio')
        self.parent=ppal
        self.setup()
    def setup(self):
        self.grafica=MyGraphCanvas(self)
        self.grafica.cargar_ekg(self.fs,self.fp,self.fqrs,self.inicio,self.fin)
        self.verticalLayout.addWidget(self.grafica)
        self.salir.clicked.connect(self.salir1)
        self.boton.clicked.connect(self.diagnostico1)
    def salir1(self):
        self.parent.show()
        self.close()
    def diagnostico1(self):
        diag=self.parent.cargarDiagnostico(self.fs,self.fp,self.fqrs,self.inicio,self.fin)
        self.diagnostico.setText(diag)
        self.boton.setEnabled(False)

class MyGraphCanvas(FigureCanvas):
    #constructor
    def __init__(self,ppal=None):
        self.fig , self.ax = plt.subplots(facecolor='gray')
        FigureCanvas.__init__(self,self.fig)
        self.ax.margins(x=0)
        self.ax.grid(True)
        self.cargar_ekg()
    #hay que crear un metodo para graficar lo que quiera
    def cargar_ekg(self, fs=1000, f_p=1, f_qrs=0.5, pr_interval_start=0.1, pr_interval_end=0.8):
        t = np.linspace(int(pr_interval_start), int(pr_interval_end), int(fs))  # Tiempo de 0 a 1 segundo
        ecg_signal = (
                np.sin(2 * np.pi * int(f_p) * t) +  # Onda P
                np.sin(2 * np.pi * float(f_qrs) * t)  # Complejo QRS
        ) * 0.5  # Amplitud reducida para una mejor visualización
        self.ax.plot(t, ecg_signal, color='black', label='Señal de EKG')
        self.ax.fill_betweenx(
            y=[np.min(ecg_signal), np.max(ecg_signal)],
            x1=float(pr_interval_start),
            x2=float(pr_interval_end),
            color='lightblue',
            alpha=0.5,
            label='Intervalo PR'
        )
        self.ax.set_xlabel('Tiempo (s)')
        self.ax.set_ylabel('Amplitud')
        self.ax.set_title('Señal de EKG con Intervalo PR')
        self.draw()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_canvas = MyGraphCanvas()
    my_canvas.show()
    sys.exit(app.exec_())