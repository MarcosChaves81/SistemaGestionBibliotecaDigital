
class MetaEntidad(type):
  
    def __new__(cls, nombre, bases, atributos):  # Todas las clases que hereden de EntidadBase deben implementar mostrar_info()

        if nombre != "EntidadBase" and "mostrar_info" not in atributos:
            raise TypeError(
                f"La clase '{nombre}' debe implementar el método mostrar_info()."
            )

        return super().__new__(cls, nombre, bases, atributos)