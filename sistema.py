from patrones.singleton import Singleton
from gestores.gestor_libros import GestionLibros
from gestores.gestor_usuarios import GestionUsuarios
from gestores.gestor_prestamos import GestionPrestamos
from modelos.administrador import Administrador

class SistemaBiblioteca(Singleton):
    def __init__(self):
        if hasattr(self, "_inicializado"):
            return

        self.admin = Administrador(
            "Admin",
            "Sistema",
            "00000000",
            "admin@sistema.com"
        )

        self.gestion_libros = GestionLibros()
        self.gestion_usuarios = GestionUsuarios()
        self.gestion_prestamos = GestionPrestamos(
            self.gestion_libros,
            self.gestion_usuarios
        )

        self._inicializado = True

    def mostrar_admin(self):
        return self.admin.mostrar_info()