def dias_vividos(edad: int) -> int:
    """
    Calcula la cantidad de días vividos, asumiendo 365 días por año.

    Args:
        edad (int): La edad en años.

    Returns:
        int: El número aproximado de días vividos.
    """
    return edad * 365


def main():
    """
    Función principal que solicita datos al usuario, calcula los días
    vividos y muestra el resultado.
    """
    print("Iniciando la aplicación CLI...", flush=True)
    nombre = input("¿Cuál es tu nombre? ")
    edad_str = input("¿Cuántos años tienes? ")

    try:
        edad = int(edad_str)
    except ValueError:
        print("Por favor, ingresa un número válido para la edad.")
        return

    dias = dias_vividos(edad)
    print(f"{nombre}, has vivido aproximadamente {dias} días.")


if __name__ == '__main__':
    main()
