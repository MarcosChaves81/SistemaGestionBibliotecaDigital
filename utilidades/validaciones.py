def validar_campo_obligatorio(valor: str, nombre_campo: str) -> str:
    valor = valor.strip() #quita espacios al priincippio y al final

    if not valor:
        raise ValueError(f"El campo {nombre_campo} no puede estar vacío.")

    return valor #devuelve el valor sin espacios al principio y al final


def validar_nombre(valor: str, nombre_campo: str) -> str:
    valor = validar_campo_obligatorio(valor, nombre_campo)

    texto_sin_espacios = valor.replace(" ", "")

    if not texto_sin_espacios.isalpha():
        raise ValueError(
            f"El campo {nombre_campo} solo puede contener letras y espacios."
        )

    return valor


def validar_dni(valor: str) -> str:
    valor = validar_campo_obligatorio(valor, "DNI")

    if not valor.isdigit():
        raise ValueError("El DNI solo puede contener números.")

    return valor


def validar_email(valor: str) -> str:
    valor = validar_campo_obligatorio(valor, "email")

    if "@" not in valor or "." not in valor:
        raise ValueError("El email debe contener '@' y '.'.")

    return valor