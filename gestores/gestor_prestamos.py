from modelos.prestamo import Prestamo
from decoradores.decorador import anunciar_accion

ARCHIVO = "prestamos.txt"

class GestionPrestamos:
    def __init__(self, gestor_libros, gestor_usuarios):
        self._gestor_libros = gestor_libros
        self._gestor_usuarios = gestor_usuarios
        self._prestamos = []

    def buscar_prestamo_activo(self, isbn):
        for prestamo in self._prestamos:
            if prestamo.libro.isbn == isbn and prestamo.fecha_devolucion is None:
                return prestamo
        return None
