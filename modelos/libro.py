from utilidades.validaciones import validar_campo_obligatorio, validar_anio, validar_cantidad_paginas
from modelos.entidad_base import EntidadBase 
class Libro(EntidadBase):
    def __init__(self, titulo:str, autor:str, isbn:str, anio_publicacion:int, cantidad_paginas:int):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.anio_publicacion = anio_publicacion
        self.cantidad_paginas = cantidad_paginas
        self._disponible = True

    @property
    def titulo(self):
        return self._titulo
    @titulo.setter
    def titulo(self, valor):        
        self._titulo = validar_campo_obligatorio(valor, "Titulo")

    @property
    def autor(self):
        return self._autor
    @autor.setter
    def autor(self, valor):
        self._autor = validar_campo_obligatorio(valor, "Autor")

    @property   
    def isbn(self):
        return self._isbn
    @isbn.setter
    def isbn(self, valor):
        self._isbn = validar_campo_obligatorio(valor, "ISBN")

    @property   
    def anio_publicacion(self):
        return self._anio_publicacion
    @anio_publicacion.setter
    def anio_publicacion(self, valor):
        self._anio_publicacion = validar_anio(valor)

    @property   
    def cantidad_paginas(self):
        return self._cantidad_paginas
    @cantidad_paginas.setter
    def cantidad_paginas(self, valor):
        self._cantidad_paginas = validar_cantidad_paginas(valor)



    @property
    def disponible(self):
        return self._disponible

    def marcar_prestado(self):

        if not self.disponible:
            raise ValueError("El libro ya se encuentra prestado.")

        self._disponible = False
        
    def marcar_disponible(self):

        if self.disponible:
            raise ValueError("El libro ya se encuentra disponible.")

        self._disponible = True
    

    def mostrar_info(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Año de Publicación: {self.anio_publicacion},Cantidad de Páginas: {self.cantidad_paginas}, Disponible: {self.disponible}"
    