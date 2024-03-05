class Pasajero:
    def __init__(self,nombre,apellido,edad,pasaporte):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.pasaporte=pasaporte
    def mostrarInformacion(self):
        print(f'El nombre de la persona a es {self.nombre} {self.apellido} y su edad es {self.edad}')       
class reservaVuelos:
    vuelos=[]
    def __init__(self,aerolinea):
        self.aerolinea=aerolinea
    @classmethod
    def adicionVuelos(cls,vuelo):
        if vuelo in cls.vuelos:
            print(f'El vuelo {vuelo.numeroVuelo} ya se ha agregado')
        else:
            cls.vuelos.append(vuelo)
            print('Vuelo añadido')
    def buscarVuelo(self,numeroVuelo):
        for i in range(len(reservaVuelos.vuelos)):
            if reservaVuelos.vuelos[i].numeroVuelo==numeroVuelo:
                return f"""Vuelo Encontrado:
                      {reservaVuelos.vuelos[i].mostrarInformacion()}"""
                break
            elif i==range(len(reservaVuelos.vuelos)):
                print(f'El vuelo {numeroVuelo} no ha sido encontrado')
    def vuelosDisponibles(self):
        for j in reservaVuelos.vuelos:
            print(j.mostrarInformacion)
    # def presentarVuelos(self):
    def realizarReserva(self,pasajero,vuelo):
        return vuelo.reservarAsiento(pasajero)
    def cancelarReserva(self,pasajero,vuelo):
        return vuelo.cancelarReserva(pasajero)
class Vuelo:
    def __init__(self,numeroVuelo,origen,destino,capacidadTotal):
        self.numeroVuelo=numeroVuelo
        self.origen=origen
        self.destino=destino
        self.capacidadTotal=capacidadTotal
        self.asientosDisponibles=capacidadTotal
        self.reservas=[]# Se pone acá ya que es una lista de reservas de un vuelo en concreto
        reservaVuelos.adicionVuelos(self) #Relación de dependencia
    def mostrarInformacion(self):
        print(f"El vuelo {self.numeroVuelo} con origen {self.origen} y destino {self.destino} tiene {self.asientosDisponibles} asientos disponibles de {self.capacidadTotal}.")
    def reservarAsiento(self,pasajero): #Asociación
        if pasajero in self.reservas:
            print(f"El usuario {pasajero} ya tiene una reserva en este vuelo")
        elif self.asientosDisponibles>0:
            self.reservas.append(pasajero)
            self.asientosDisponibles-=1
            print(f'El usuario {pasajero.nombre} {pasajero.apellido} ha sido agregado adecuadamente a el vuelo {self.numeroVuelo} de origen {self.origen} con destino a {self.destino}.')
        else:
            print(f'El vuelo {self.numeroVuelo} no tiene asientos disponibles')
    def cancelarReserva(self,pasajero):
        if pasajero in self.reservas:
            self.reservas.remove(pasajero)
            self.asientosDisponibles+=1
            print(f'El pasajero {pasajero.nombre} {pasajero.apellido} ha cancelado adecuadamente su vuelo {self.numeroVuelo}.')
        else:
            print(f'La persona {pasajero.nombre} {pasajero.apellido} no tiene una reserva')
pasajero1=Pasajero('Pablo','Aristizábal',18,'PP123')
# pasajero1.mostrarInformacion()
vuelo1=Vuelo('AJ895',"Madrid","Shangai",100)
latam=reservaVuelos('Latam')
# vuelo1.mostrarInformacion()
print('_'*100)
# latam.buscarVuelo('AJ895')
vuelo2=Vuelo('JJ555','Medellín','Bogotá',40)