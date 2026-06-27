from datetime import datetime #importo datetime para obtener la fecha actual
from modelos.usuario import Usuario #importo la clase Usuario
from modelos.libro import Libro #importo la clase Libro    

class Prestamo:
    def __init__(self,usuario:Usuario, libro:Libro):
        if not libro.disponible:
            raise ValueError("El libro no está disponible")

        self._usuario = usuario
        self._libro = libro
        self._fecha_prestamo = datetime.now() #fecha actual
        self._libro.marcar_prestado()
        self._fecha_devolucion = None



    def devolver(self):
        if self._fecha_devolucion is not None:
            raise ValueError("El libro ya fue devuelto")

        self._fecha_devolucion = datetime.now()
        self._libro.marcar_disponible()

    @property
    def usuario(self):
        return self._usuario
    
    @property
    def libro(self):
        return self._libro
    
    @property
    def fecha_prestamo(self):
        return self._fecha_prestamo 
    
    @property
    def fecha_devolucion(self):
        return self._fecha_devolucion