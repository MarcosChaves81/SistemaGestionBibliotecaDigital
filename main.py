from sistema import SistemaBiblioteca

CLAVE_ADMIN = "admin"
CLAVE_USUARIO = "1234"

def login():
    sistema = SistemaBiblioteca()
    print("=== SISTEMA DE BIBLIOTECA DIGITAL ===")
    print("1. Ingresar como Administrador")
    print("2. Ingresar como Usuario")
    print("0. Salir")
    opcion = input("Seleccione: ")

    if opcion == "1":
        clave = input("Ingrese la clave de administrador: ")
        if clave == CLAVE_ADMIN:
            print("Acceso concedido.")
            return "admin", sistema
        else:
            print("Clave incorrecta.")
            return None, None

    elif opcion == "2":
        dni = input("Ingrese su DNI: ")
        clave = input("Ingrese su clave: ")
        usuario = sistema.gestion_usuarios.buscar_por_dni(dni)
        if usuario and clave == CLAVE_USUARIO:
            print(f"Bienvenido, {usuario.nombre}.")
            return "usuario", sistema
        else:
            print("DNI o clave incorrectos.")
            return None, None

    elif opcion == "0":
        print("Saliendo...")
        exit()

if __name__ == "__main__":
    rol, sistema = login()

