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

   @anunciar_accion("registró")
    def registrar_prestamo(self, admin, dni, isbn):
        usuario = self._gestor_usuarios.buscar_por_dni(dni)
        if not usuario:
            raise ValueError(f"No se encontró un usuario con DNI {dni}")
        libro = self._gestor_libros.buscar_por_isbn(isbn)
        if not libro:
            raise ValueError(f"No se encontró un libro con ISBN {isbn}")
        if self.buscar_prestamo_activo(isbn):
            raise ValueError("El libro ya tiene un préstamo activo")
        prestamo = Prestamo(usuario, libro)
        self._prestamos.append(prestamo)
        
