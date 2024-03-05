class Pasajero:
    def __init__(self,nombre,apellido,edad,pasaporte):
        self._nombre=nombre
        self._apellido=apellido
        self._edad=edad
        self.__pasaporte=pasaporte
    def mostrarInformacion(self):
        print(f'El nombre de la persona a es {self._nombre} {self._apellido} y su edad es {self._edad}')       
class reservaVuelos:
    def __init__(self,aerolinea):
        self.aerolinea=aerolinea
    # def adicionVuelos(self):
    # def buscaeVuelo(self):
    # def presentarVuelos(self):
    # def realizarReserva(self):
    # def cancelarReserva(self):
class Vuelo:
    def __init__(self,numeroVuelo,origen,destino,capacidadTotal):
        self.numeroVuelo=numeroVuelo
        self.origen=origen
        self.destino=destino
        self.capacidadTotal=capacidadTotal
        self.asientosDisponibles=capacidadTotal
        self.reservas=[]# Se pone acá ya que es una lista de reservas de un vuelo en concreto
    def mostrarInformacion(self):
        print(f"El vuelo {self.numeroVuelo} con origen {self.origen} y destino {self.destino} tiene {self.asientosDisponibles} asientos disponibles de {self.capacidadTotal}.")
    def reservarAsiento(self,pasajero): #Asociación
        if pasajero in self.reservas:
            print(f"El usuario {pasajero} ya tiene una reserva en este vuelo")
        elif self.asientosDisponibles>0:
            self.reservas.append(pasajero)
            self.asientosDisponibles-=1
            print(f'El usuario {pasajero} ha sido agregado adecuadamente a el vuelo {self.numeroVuelo} de origen {self.origen} con destino a {self.destino}.')
        else:
            print(f'El vuelo {self.numeroVuelo} no tiene asientos disponibles')
pasajero1=Pasajero('Pablo','Aristizábal',18,'PP123')
# pasajero1.mostrarInformacion()
vuelo1=Vuelo('AJ895',"Madrid","Shangai",100)
vuelo1.mostrarInformacion()
vuelo1.reservarAsiento(pasajero1)
vuelo1.mostrarInformacion()