import json

class Modelo(object):
    def __init__(self):
        self.__usuarios = {}
        #se crea un usuario inicial para arrancar el sistema
        self.__usuarios['contrasena123'] = 'admin123'
    def verificarAdministrador(self, u, p):
        try:
            #Si existe la clave se verifica que sea el usuario
            if self.__usuarios[p] == u:
                return True
            else:
                return False
        except: #si la clave no existe para evitar KeyError
            return False   
    def registrarUsuario(self,nombre,apellido,edad,id):
        a=r'C:\Users\Pablo\Informática ll\git.repositorio\Inform-tica-ll\Talleres\Unidad 4\Usuarios.json'
        with open(a,'r') as Usuarios:
            self.__usuarios=json.load(Usuarios)
        if id in self.__usuarios.keys():
            Usuarios.close()
            return True
        else:
            with open(a,'w') as Usuarios:
                self.__usuarios[id]={
                    "Nombre": nombre.upper(),
                    "Apellido":apellido.upper(),
                    "Edad":edad
                    }
                a=str(self.__usuarios)
                json.dump(self.__usuarios, Usuarios, ensure_ascii=False, indent=2)
                Usuarios.close()
            return False