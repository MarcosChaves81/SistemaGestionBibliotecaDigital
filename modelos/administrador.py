from modelos.persona import Persona
class Administrador(Persona):
    def mostrar_info(self):
        return (
            f"Administrador\n"
            f"Nombre: {self.nombre}\n"
            f"Apellido: {self.apellido}\n"
            f"DNI: {self.dni}\n"
            f"Email: {self.email}"
        )