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

    @anunciar_accion("devolvió")
    def registrar_devolucion(self, admin, isbn):
        prestamo = self.buscar_prestamo_activo(isbn)
        if not prestamo:
            raise ValueError(f"No hay un préstamo activo para el ISBN {isbn}")
        prestamo.devolver()

    def listar_prestamos_activos(self):
        activos = [p for p in self._prestamos if p.fecha_devolucion is None]
        if not activos:
            print("No hay préstamos activos.")
            return
        for prestamo in activos:
            print(f"Usuario: {prestamo.usuario.nombre} {prestamo.usuario.apellido} | "
                  f"Libro: {prestamo.libro.titulo} | "
                  f"Fecha préstamo: {prestamo.fecha_prestamo.strftime('%d/%m/%Y')}")
        
        
