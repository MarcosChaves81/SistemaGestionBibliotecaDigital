from modelos.prestamo import Prestamo
from decoradores.decorador import anunciar_accion
from datetime import datetime

ARCHIVO = "prestamos.txt"

class GestionPrestamos:
    def __init__(self, gestor_libros, gestor_usuarios):
        self._gestor_libros = gestor_libros
        self._gestor_usuarios = gestor_usuarios
        self._prestamos = self._cargar()

    def _cargar(self):
        prestamos = []
        try:
            with open(ARCHIVO, "r", encoding="utf-8") as f:
                for linea in f:
                    linea = linea.strip()
                    if linea:
                        isbn, dni, fecha_prestamo_str, fecha_dev_str = linea.split("|")
                        libro = self._gestor_libros.buscar_por_isbn(isbn)
                        usuario = self._gestor_usuarios.buscar_por_dni(dni)
                        if libro and usuario:
                            prestamo = Prestamo(usuario, libro)
                            prestamo._fecha_prestamo = datetime.strptime(fecha_prestamo_str, "%d/%m/%Y %H:%M")
                            if fecha_dev_str != "None":
                                prestamo._fecha_devolucion = datetime.strptime(fecha_dev_str, "%d/%m/%Y %H:%M")
                                prestamo._libro.marcar_disponible()
                            prestamos.append(prestamo)
        except FileNotFoundError:
            pass
        return prestamos

    def _guardar(self):
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            for prestamo in self._prestamos:
                fecha_dev = prestamo.fecha_devolucion.strftime("%d/%m/%Y %H:%M") if prestamo.fecha_devolucion else "None"
                f.write(f"{prestamo.libro.isbn}|{prestamo.usuario.dni}|{prestamo.fecha_prestamo.strftime('%d/%m/%Y %H:%M')}|{fecha_dev}\n")

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
        self._guardar()

    @anunciar_accion("devolvió")
    def registrar_devolucion(self, admin, isbn):
        prestamo = self.buscar_prestamo_activo(isbn)
        if not prestamo:
            raise ValueError(f"No hay un préstamo activo para el ISBN {isbn}")
        prestamo.devolver()
        self._guardar()

    def listar_prestamos_activos(self):
        activos = [p for p in self._prestamos if p.fecha_devolucion is None]
        if not activos:
            print("No hay préstamos activos.")
            return
        for prestamo in activos:
            print(f"Usuario: {prestamo.usuario.nombre} {prestamo.usuario.apellido} | "
                  f"Libro: {prestamo.libro.titulo} | "
                  f"Fecha préstamo: {prestamo.fecha_prestamo.strftime('%d/%m/%Y')}")
            
        
