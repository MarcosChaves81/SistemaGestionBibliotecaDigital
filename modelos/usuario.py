class Usuario(Persona):
   
    def mostrar_info(self):
        return f"Nombre:{self.nombre}, apellido:{self.apellido},DNI:{self.dni}, email:{self.email}"
