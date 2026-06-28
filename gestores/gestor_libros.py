from modelos.libro import Libro
from decoradores.decorador import anunciar_accion

ARCHIVO = "libros.txt"

class GestionLibros:
    def __init__(self):
        self._libros = self._cargar()

    def _cargar(self):
        libros = []
        try:
            with open(ARCHIVO, "r", encoding="utf-8") as f:
                for linea in f:
                    linea = linea.strip()
                    if linea:
                        titulo, autor, isbn, anio, paginas = linea.split("|")
                        libros.append(Libro(titulo, autor, isbn, int(anio), int(paginas)))
        except FileNotFoundError:
            pass
        return libros

    def _guardar(self):
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            for libro in self._libros:
                f.write(f"{libro.titulo}|{libro.autor}|{libro.isbn}|{libro.anio_publicacion}|{libro.cantidad_paginas}\n")

    def buscar_por_isbn(self, isbn):
        for libro in self._libros:
            if libro.isbn == isbn:
                return libro
        return None

    @anunciar_accion("agregó")
    def agregar(self, admin, titulo, autor, isbn, anio, paginas):
        if self.buscar_por_isbn(isbn):
            raise ValueError(f"Ya existe un libro con ISBN {isbn}")
        libro = Libro(titulo, autor, isbn, anio, paginas)
        self._libros.append(libro)
        self._guardar()

 @anunciar_accion("eliminó")
    def eliminar(self, admin, isbn):
        libro = self.buscar_por_isbn(isbn)
        if not libro:
            raise ValueError(f"No se encontró un libro con ISBN {isbn}")
        if not libro.disponible:
            raise ValueError("No se puede eliminar un libro que está prestado")
        self._libros.remove(libro)
        self._guardar()
        

  
