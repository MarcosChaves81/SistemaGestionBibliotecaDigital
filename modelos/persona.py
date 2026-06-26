from abc import ABC, abstractmethod
from utilidades.validaciones import validar_nombre, validar_dni, validar_email

class Persona(ABC):
    def __init__(self,nombre:str,apellido:str,dni:str,email:str):
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.email=email

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = validar_nombre(valor, "Nombre")

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, valor):
        self._apellido = validar_nombre(valor, "Apellido")

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, valor):
        self._dni = validar_dni(valor)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):     
        self._email = validar_email(valor)


    @abstractmethod
    def mostrar_info(self):
        pass



