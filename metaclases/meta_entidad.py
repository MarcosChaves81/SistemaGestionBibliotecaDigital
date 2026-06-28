
class MetaEntidad(type):
  
    def __new__(cls, nombre, bases, atributos):

        if nombre != "EntidadBase" and "mostrar_info" not in atributos:
            raise TypeError(
                f"La clase '{nombre}' debe implementar el método mostrar_info()."
            )

        return super().__new__(cls, nombre, bases, atributos)