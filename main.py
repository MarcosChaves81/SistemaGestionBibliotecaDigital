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

def menu_admin(sistema):
    while True:
        print("\n=== MENÚ ADMINISTRADOR ===")
        print("1. Gestionar libros")
        print("2. Gestionar usuarios")
        print("3. Ver préstamos activos")
        print("0. Cerrar sesión")
        opcion = input("Seleccione: ")

        if opcion == "1":
            while True:
                print("\n--- LIBROS ---")
                print("1. Agregar libro")
                print("2. Eliminar libro")
                print("3. Modificar libro")
                print("4. Listar libros")
                print("0. Volver")
                op = input("Seleccione: ")
                if op == "1":
                    titulo = input("Título: ")
                    autor = input("Autor: ")
                    isbn = input("ISBN: ")
                    anio = int(input("Año: "))
                    paginas = int(input("Páginas: "))
                    sistema.gestion_libros.agregar("Admin", titulo, autor, isbn, anio, paginas)
                elif op == "2":
                    isbn = input("ISBN a eliminar: ")
                    sistema.gestion_libros.eliminar("Admin", isbn)
                elif op == "3":
                    isbn = input("ISBN a modificar: ")
                    titulo = input("Nuevo título (Enter para omitir): ") or None
                    autor = input("Nuevo autor (Enter para omitir): ") or None
                    anio = input("Nuevo año (Enter para omitir): ")
                    anio = int(anio) if anio else None
                    paginas = input("Nuevas páginas (Enter para omitir): ")
                    paginas = int(paginas) if paginas else None
                    sistema.gestion_libros.modificar("Admin", isbn, titulo, autor, anio, paginas)
                elif op == "4":
                    sistema.gestion_libros.listar()
                elif op == "0":
                    break

        elif opcion == "2":
            while True:
                print("\n--- USUARIOS ---")
                print("1. Agregar usuario")
                print("2. Eliminar usuario")
                print("3. Modificar usuario")
                print("4. Listar usuarios")
                print("0. Volver")
                op = input("Seleccione: ")
                if op == "1":
                    nombre = input("Nombre: ")
                    apellido = input("Apellido: ")
                    dni = input("DNI: ")
                    email = input("Email: ")
                    sistema.gestion_usuarios.agregar("Admin", nombre, apellido, dni, email)
                elif op == "2":
                    dni = input("DNI a eliminar: ")
                    sistema.gestion_usuarios.eliminar("Admin", dni)
                elif op == "3":
                    dni = input("DNI a modificar: ")
                    nombre = input("Nuevo nombre (Enter para omitir): ") or None
                    apellido = input("Nuevo apellido (Enter para omitir): ") or None
                    email = input("Nuevo email (Enter para omitir): ") or None
                    sistema.gestion_usuarios.modificar("Admin", dni, nombre, apellido, email)
                elif op == "4":
                    sistema.gestion_usuarios.listar()
                elif op == "0":
                    break

        elif opcion == "3":
            sistema.gestion_prestamos.listar_prestamos_activos()

        elif opcion == "0":
            print("Cerrando sesión...")
            break

if __name__ == "__main__":
    rol, sistema = login()
    if rol == "admin":
        menu_admin(sistema)


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

def menu_admin(sistema):
    while True:
        print("\n=== MENÚ ADMINISTRADOR ===")
        print("1. Gestionar libros")
        print("2. Gestionar usuarios")
        print("3. Ver préstamos activos")
        print("0. Cerrar sesión")
        opcion = input("Seleccione: ")

        if opcion == "1":
            while True:
                print("\n--- LIBROS ---")
                print("1. Agregar libro")
                print("2. Eliminar libro")
                print("3. Modificar libro")
                print("4. Listar libros")
                print("0. Volver")
                op = input("Seleccione: ")
                if op == "1":
                    titulo = input("Título: ")
                    autor = input("Autor: ")
                    isbn = input("ISBN: ")
                    anio = int(input("Año: "))
                    paginas = int(input("Páginas: "))
                    sistema.gestion_libros.agregar("Admin", titulo, autor, isbn, anio, paginas)
                elif op == "2":
                    isbn = input("ISBN a eliminar: ")
                    sistema.gestion_libros.eliminar("Admin", isbn)
                elif op == "3":
                    isbn = input("ISBN a modificar: ")
                    titulo = input("Nuevo título (Enter para omitir): ") or None
                    autor = input("Nuevo autor (Enter para omitir): ") or None
                    anio = input("Nuevo año (Enter para omitir): ")
                    anio = int(anio) if anio else None
                    paginas = input("Nuevas páginas (Enter para omitir): ")
                    paginas = int(paginas) if paginas else None
                    sistema.gestion_libros.modificar("Admin", isbn, titulo, autor, anio, paginas)
                elif op == "4":
                    sistema.gestion_libros.listar()
                elif op == "0":
                    break

        elif opcion == "2":
            while True:
                print("\n--- USUARIOS ---")
                print("1. Agregar usuario")
                print("2. Eliminar usuario")
                print("3. Modificar usuario")
                print("4. Listar usuarios")
                print("0. Volver")
                op = input("Seleccione: ")
                if op == "1":
                    nombre = input("Nombre: ")
                    apellido = input("Apellido: ")
                    dni = input("DNI: ")
                    email = input("Email: ")
                    sistema.gestion_usuarios.agregar("Admin", nombre, apellido, dni, email)
                elif op == "2":
                    dni = input("DNI a eliminar: ")
                    sistema.gestion_usuarios.eliminar("Admin", dni)
                elif op == "3":
                    dni = input("DNI a modificar: ")
                    nombre = input("Nuevo nombre (Enter para omitir): ") or None
                    apellido = input("Nuevo apellido (Enter para omitir): ") or None
                    email = input("Nuevo email (Enter para omitir): ") or None
                    sistema.gestion_usuarios.modificar("Admin", dni, nombre, apellido, email)
                elif op == "4":
                    sistema.gestion_usuarios.listar()
                elif op == "0":
                    break

        elif opcion == "3":
            sistema.gestion_prestamos.listar_prestamos_activos()

        elif opcion == "0":
            print("Cerrando sesión...")
            break

def menu_usuario(sistema, usuario):
    while True:
        print(f"\n=== MENÚ USUARIO — {usuario.nombre} {usuario.apellido} ===")
        print("1. Buscar libro por ISBN")
        print("2. Pedir préstamo")
        print("3. Devolver libro")
        print("0. Cerrar sesión")
        opcion = input("Seleccione: ")

        if opcion == "1":
            isbn = input("ISBN a buscar: ")
            libro = sistema.gestion_libros.buscar_por_isbn(isbn)
            if libro:
                print(libro.mostrar_info())
            else:
                print("Libro no encontrado.")

        elif opcion == "2":
            isbn = input("ISBN del libro a pedir: ")
            try:
                sistema.gestion_prestamos.registrar_prestamo("Usuario", usuario.dni, isbn)
                print("Préstamo registrado con éxito.")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "3":
            isbn = input("ISBN del libro a devolver: ")
            try:
                sistema.gestion_prestamos.registrar_devolucion("Usuario", isbn)
                print("Devolución registrada con éxito.")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "0":
            print("Cerrando sesión...")
            break

if __name__ == "__main__":
    rol, sistema = login()
    if rol == "admin":
        menu_admin(sistema)
    elif rol == "usuario":
        usuario = sistema.gestion_usuarios.buscar_por_dni(input("Reingrese su DNI: "))
        menu_usuario(sistema, usuario)




