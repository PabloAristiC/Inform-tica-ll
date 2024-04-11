import datetime 
from datetime import datetime as dt
import pprint as pp
def validar_fecha(fecha):
    '''
    verifica que el usuario ingrese una fecha válida en el formato pedido
    '''
    while True:
        try:
            fecha_formato = dt.strptime(fecha, '%d/%m/%Y')            
            print("La fecha ingresada es válida")
            print('-'*50)
            return fecha        
        except ValueError:
            print("El formato de la fecha ingresada no es válido. Debe ingresarse en formato dd/mm/yyyy")
            print('-'*50)
            fecha=input('Ingrese una fecha con el formato dd/mm/aaaa\n')
def validar(valor,tipo):
    '''
    Esta función tiene dos entradas, la primera es el input el cual se va a validar y la segunda es el tipo de input esperado, ya sea str o int
    '''
    while True:
        try:
            if tipo==int:
                if valor.isdigit():
                    return valor
                else:
                    print('-'*50)
                    print('Error, debe ingresar un número entero')
                    print('-'*50)
                    valor=input('Ingresar el valor nuevamente\n')
                    print('-'*50)
            elif tipo==str:
                if valor.isalpha():
                    return valor
                else:
                    print('-'*50)
                    print('Error, debe ingresar solo texto')
                    print('-'*50)
                    valor=input('Ingresar el valor nuevamente\n')
                    print('-'*50)
            else:
                return valor
        except:
            print('-'*50)
            print('Error, no ingresó el valor solicitado tipo'+str(tipo))
            Valor=input('Ingresar el valor nuevamente\n')
            print('-'*50)
class Implantes:
    implantes=[]
    def __init__(self, implante, estado, paciente, medico, fecha):       
        self._implante=implante
        self._estado = estado
        self._paciente = paciente
        self._medico = medico
        self._fecha=fecha  
    @classmethod
    def adicionImplante(cls,implante):
        if implante in cls.implantes:
            print(f'El implante {implante} ya se ha agregado')
        else:
            cls.implantes.append(implante)
            print('Implante añadido correctamente')
    @property
    def estado(self):
        return self._estado
    @estado.setter  
    def estado(self,estado): 
        self._estado=estado
    @property
    def fechaRevision(self):
        return self._fechaRevision
    @fechaRevision.setter  
    def fechaRevision(self,fecha): 
        self._fechaRevision=fecha
    @property
    def paciente(self):
        return self._paciente
    @paciente.setter  
    def paciente(self,paciente): 
        self._pacientes.append(paciente)
        self._paciente=paciente
    @property
    def medico(self):
        return self._medico
    @medico.setter  
    def medico(self,medico): 
        self._medico=medico
    @property
    def fecha(self):
        return self._fecha
    @fecha.setter  
    def fecha(self,fecha): 
        self._fecha=fecha
    def infoImplante_ocupado(self):
        return f'El implante {self._implante} está {self._estado} por {self._paciente}, que fue asignado por {self._medico} el día {self._fecha}.'
    def infoImplante_desocupado(self):
        return f'El implante {self._implante} está {self._estado} y fue revisado por última vez el día {self._fechaRevision}.'
class Cadera(Implantes):
    def __init__(self,implante,estado,paciente,medico,fecha,material,fijacion,tamaño):
        Implantes.__init__(self,implante,estado,paciente,medico,fecha)
        self._material=material
        self._fijacion=fijacion
        self._tamaño=tamaño
        Implantes.adicionImplante(implante)
class Rodilla(Implantes):
    def __init__(self,implante,estado,paciente,medico,fecha,material,fijacion,tamaño):
        Implantes.__init__(self,implante,estado,paciente,medico,fecha)
        self._material=material
        self._fijacion=fijacion
        self._tamaño=tamaño
        Implantes.adicionImplante(implante)
class Dental(Implantes):
    def __init__(self,implante,estado,paciente,medico,fecha,material,fijacion,forma):
        Implantes.__init__(self,implante,estado,paciente,medico,fecha)
        self._material=material
        self._fijacion=fijacion
        self._forma=forma
        Implantes.adicionImplante(implante)
class Coronario(Implantes):
    def __init__(self,implante,estado,paciente,medico,fecha,material,longitud,diametro):
        Implantes.__init__(self,implante,estado,paciente,medico,fecha)
        self._material=material
        self._longitud=longitud
        self._diametro=diametro
        Implantes.adicionImplante(implante)
class Marcapasos(Implantes):
    def __init__(self,implante,estado,paciente,medico,fecha,electrodos,tipo,frecuencia):  #tipo es alámbrico o inalámbrico
        Implantes.__init__(self,implante,estado,paciente,medico,fecha)
        self._electrodos=electrodos
        self._tipo=tipo
        self._frecuencia=frecuencia
        Implantes.adicionImplante(implante)
print('Bienvenido al sistema de gestión de implantes médicos')
coleccionImplantes=[]
while True:
    print('_'*50)
    menu=input('Ingrese la opción (en número) a la que desea ingresar:\n1. Agregar Implante.\n2. Eliminar implante.\n3. Editar información de implante.\n4. Ver todos los implantes.\n5. Salir.\n')
    validar(menu,int)
    print('_'*50)
    if menu=='1':
        tipo=input('Ingrese e tipo de implante a ingresar:\n1. Implante de cadera\n2. Implante de rodilla\n3. Implante dental\n4.Implante coronario\n5. Marcapasos.\n6. Salir.\n')
        validar(tipo,int)
        print('_'*50)
        while True:
            if tipo=='1':
                implante=input('Ingrese el nombre del implante de cadera\n')
                validar(implante,str)
                print('_'*50)
                estado='Disponible'
                paciente=None
                medico=None
                fecha=None
                material=input("Ingrese el material del implante de cadera\n")
                validar(material,str)
                print('_'*50)
                fijacion=input('Ingrese el tipo de fijación del implante de cadera\n')
                validar(fijacion,str)
                print('_'*50)
                tamaño=input('Ingrese el tamaño del implante:\n1. Grande\n2. Mediano\n3. Pequeño.\n')
                validar(tamaño,int)
                print('_'*50)
                while True:
                    if tamaño=='1':
                        Tamaño='Grande'
                        break
                    elif tamaño=='2':
                        Tamaño='Mediano'
                        break
                    elif tamaño=='3':
                        Tamaño='Pequeño'
                        break
                    else:
                        print('Valor no válido, por favor ingrese bien el tamaño del implante')
                        tamaño=input('Ingrese el tamaño del implante:\n1. Grande\2. Mediano\n3. Pequeño\n')
                        validar(tamaño,int)
                        print('_'*50)
                implanteCadera=Cadera(implante,estado,paciente,medico,fecha,material,fijacion,Tamaño)
                implante_cadera=[implante,estado,paciente,medico,fecha,material,fijacion,Tamaño]
                coleccionImplantes.append(implante_cadera)
                break
            elif tipo=='2':
                implante=input('Ingrese el nombre del implante de rodilla\n')
                validar(implante,str)
                print('_'*50)
                estado='Disponible'
                paciente=None
                medico=None
                fecha=None
                material=input("Ingrese el material del implante de rodilla\n")
                validar(material,str)
                print('_'*50)
                fijacion=input('Ingrese el tipo de fijación del implante de rodilla\n')
                validar(fijacion,str)
                print('_'*50)
                tamaño=input('Ingrese el tamaño del implante:\n1. Grande\n2. Mediano\n3. Pequeño\n')
                validar(tamaño,int)
                print('_'*50)
                while True:
                    if tamaño=='1':
                        Tamaño='Grande'
                        break
                    elif tamaño=='2':
                        Tamaño='Mediano'
                        break
                    elif tamaño=='3':
                        Tamaño='Pequeño'
                        break
                    else:
                        print('Valor no válido, por favor ingrese bien el tamaño del implante')
                        tamaño=input('Ingrese el tamaño del implante:\n1. Grande\2. Mediano\n3. Pequeño\n')
                        validar(tamaño,int)
                        print('_'*50)
                implanteRodilla=Rodilla(implante,estado,paciente,medico,fecha,material,fijacion,Tamaño)
                coleccionImplantes.append(implanteRodilla)
                break
            elif tipo=='3':
                implante=input('Ingrese el nombre del implante dental\n')
                validar(implante,str)
                print('_'*50)
                estado='Disponible'
                paciente=None
                medico=None
                fecha=None
                material=input("Ingrese el material del implante dental\n")
                validar(material,str)
                print('_'*50)
                fijacion=input('Ingrese el tipo de fijación del implante dental\n')
                validar(fijacion,str)
                print('_'*50)
                forma=input('Ingrese la forma del implante:\n1. Cuadrada\2. Circular\n3. Triangular\n')
                validar(forma,int)
                print('_'*50)
                while True:
                    if forma=='1':
                        Forma='Cuadrada'
                        break
                    elif forma=='2':
                        Forma='Circular'
                        break
                    elif forma=='3':
                        Forma='Triangular'
                        break
                    else:
                        print('Valor no válido, por favor ingrese bien la forma del implante')
                        forma=input('Ingrese el tamaño del implante:\n1. Cuadrada\2. Circular\n3. Triangular\n')
                        validar(forma,int)
                        print('_'*50)
                implanteDental=Dental(implante,estado,paciente,medico,fecha,material,fijacion,Forma)
                coleccionImplantes.append(implanteDental)
                break
            elif tipo=='4':
                implante=input('Ingrese el nombre del implante coronario\n')
                validar(implante,str)
                print('_'*50)
                estado='Disponible'
                paciente=None
                medico=None
                fecha=None
                material=input("Ingrese el material del implante coronario\n")
                validar(material,str)
                print('_'*50)
                longitud=input('Ingrese la longitud del implante coronario en un número entero\n')
                validar(longitud,int)
                print('_'*50)
                diametro=input('Ingrese el diámetro del implante en un número entero\n')
                validar(diametro,int)
                print('_'*50)
                implanteCoronario=Coronario(implante,estado,paciente,medico,fecha,material,longitud,diametro)
                coleccionImplantes.append(implanteCoronario)
                break
            elif tipo=='5':
                implante=input('Ingrese el nombre del marcapasos\n')
                validar(implante,str)
                print('_'*50)
                estado='Disponible'
                paciente=None
                medico=None
                fecha=None
                electrodos=input("Ingrese el número de elctrodos del marcapasos\n")
                validar(electrodos,int)
                print('_'*50)
                frecuencia=input('Ingrese la la frecuencia del marcapasos\n')
                validar(frecuencia,int)
                print('_'*50)
                especie=input('Ingrese el tipo del marcapasos:\n1. Alámbrico\2. Inalámbrico\n')
                validar(especie,int)
                print('_'*50)
                while True:
                    if especie=='1':
                        Especie='Alámbrico'
                        break
                    elif especie=='2':
                        Especie='Inalámbrico'
                        break
                    else:
                        print('Valor no válido, por favor ingrese bien el tipo del marcapasos')
                        especie=input('Ingrese el tipo del marcapasos:\n1. Alámbrico\2. Inalámbrico')
                        validar(especie,int)
                        print('_'*50)
                implanteMarcapasos=Marcapasos(implante,estado,paciente,medico,fecha,electrodos,frecuencia,Especie)
                coleccionImplantes.append(implanteMarcapasos)
                break
            elif tipo=='6':
                break
            else:
                print('Opción no reconocida, por favor ingrese bien el número de opción')
                tipo=input('Ingrese e tipo de implante a ingresar:\n1. Implante de cadera\n2. Implante de rodilla\n3. Implante dental\n4.Implante coronario\n5. Marcapasos')
                validar(tipo,int)
                print('_'*50)
        # break
    elif menu=='2':
        nombre=input('Ingrese el nombre del implante que desea eliminar\n')
        validar(nombre,str)
        print('_'*50)
        if nombre in Implantes.implantes:
            posicion=Implantes.implantes.index(nombre)
            Implantes.implantes.remove(nombre)
            coleccionImplantes.remove(coleccionImplantes[posicion])
            print('Implante eliminado correctamente')
            print('_'*50)
        else:
            print('No existe un implante con ese nombre en los registros')
    elif menu=='3':
        accion=input('Ingrese la accion que desea realizar:\n1. Desocupar un implante\n2. Ocupar un implante\n3. Salir\n')
        validar(accion,int)
        print('_'*50)
        while True:
            if accion=='1':
                nombre=input('Ingrese el nombre del implante a desocupar\n')
                validar(nombre,str)
                print('_'*50)
                if nombre in Implantes.implantes:
                    posicion=Implantes.implantes.index(nombre)
                    if coleccionImplantes[posicion][1]=='Ocupado':
                        coleccionImplantes[posicion][1]=('Disponible')
                        coleccionImplantes[posicion][2]=None
                        coleccionImplantes[posicion][3]=None
                        coleccionImplantes[posicion][4]=None
                        print('El implante ha sido desocupado exitosamente')
                        print(coleccionImplantes[posicion])
                        break
                    else:
                        print("Error: El implante ya se encuentra desocupado")
                        break
                else:
                    print('No existe un implante con ese nombre en los registros')               
            elif accion=='2':
                nombre=input('Ingrese el nombre del implante a ocupar\n')
                print('_'*50)
                if nombre in Implantes.implantes:
                    posicion=Implantes.implantes.index(nombre)
                    if coleccionImplantes[posicion][1]=='Disponible':
                        paciente=input('Ingrese el nombre del paciente al cual se le asignara este implante\n')
                        validar(paciente,str)
                        print('_'*50)
                        medico=input('Ingrese el nombre del  médico encargado\n')
                        validar(medico,str)
                        print('_'*50)
                        fecha=input('Ingrese la fecha de implantación (dd/mm/aaaa)\n')
                        validar_fecha(fecha)
                        print('_'*50)
                        coleccionImplantes[posicion][1]='Ocupado'
                        coleccionImplantes[posicion][2]=paciente
                        coleccionImplantes[posicion][3]=medico
                        coleccionImplantes[posicion][4]=fecha
                        print('Implante actualizado correctamente')
                        print(coleccionImplantes[posicion])
                        print('_'*50)
                        break
                    else:
                        print('Error: El implante no está disponible para ser ocupado')
                        break
                else:
                    print('No existe un implante con ese nombre en los registros')
            elif accion=='3':
                break
            else:
                print('Opción no válida, por favor ingrese nuevamente la acción que desea realizar')
                accion=input('Ingrese la accion que desea realizar:\n1.Desocupar un implante\n2. Ocupar un implante\n3.Notificar mantenimiento de un implante\n4. salir\n')
            validar(accion,int)
            print('_'*50)   
    elif menu=='4':
        print(pp.pprint(coleccionImplantes))
    elif menu=='5':
        print('Gracias por utilizar el sistema de gestión de implantes')
        break
    else:
        print('Opción no válida, ingrese una opción válida para el menú')