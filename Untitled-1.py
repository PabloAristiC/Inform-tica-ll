# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         self.__nombre = nombre
#         self.__apellido = apellido
#         self.__edad = edad       
#     def nombre(self):
#         return self.__nombre
#     def apellido(self):
#         return self.apellido
#     def edad(self):
#         return self.edad
#     def set_nombre(self, nombre):
#         self.__nombre = nombre
#     def set_apellido(self, apellido):
#         self.__apellido = apellido
#     def set_edad(self, edad):
#         self.__edad = edad       
#     def __str__(self):
#         return f"{self.__nombre} {self.__apellido} tiene {self.__edad} años de edad"   
# persona1 = Persona("Pepito", "Perez", 50)
# print(persona1)
# persona1.set_nombre("Andres")
# persona1.set_edad(22)
# print(persona1)}

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad       
    def __str__(self):
        return f"{self.nombre} {self.apellido} tiene {self.edad} años de edad"   
persona1 = Persona("Pepito", "Perez", 50)
persona1.edad = 22
print(persona1)
