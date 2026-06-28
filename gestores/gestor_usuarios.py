from modelos.usuario import Usuario
from decoradores.decorador import anunciar_accion

ARCHIVO = "usuarios.txt"

class GestionUsuarios:
    def __init__(self):
        self._usuarios = self._cargar()

    def _cargar(self):
        usuarios = []
        try:
            with open(ARCHIVO, "r", encoding="utf-8") as f:
                for linea in f:
                    linea = linea.strip()
                    if linea:
                        nombre, apellido, dni, email = linea.split("|")
                        usuarios.append(Usuario(nombre, apellido, dni, email))
        except FileNotFoundError:
            pass
        return usuarios

    def _guardar(self):
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            for usuario in self._usuarios:
                f.write(f"{usuario.nombre}|{usuario.apellido}|{usuario.dni}|{usuario.email}\n")

    def buscar_por_dni(self, dni):
        for usuario in self._usuarios:
            if usuario.dni == dni:
                return usuario
        return None

@anunciar_accion("agregó")
    def agregar(self, admin, nombre, apellido, dni, email):
        if self.buscar_por_dni(dni):
            raise ValueError(f"Ya existe un usuario con DNI {dni}")
        usuario = Usuario(nombre, apellido, dni, email)
        self._usuarios.append(usuario)
        self._guardar()

 @anunciar_accion("eliminó")
    def eliminar(self, admin, dni):
        usuario = self.buscar_por_dni(dni)
        if not usuario:
            raise ValueError(f"No se encontró un usuario con DNI {dni}")
        self._usuarios.remove(usuario)
        self._guardar()
  
