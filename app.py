import os
from datetime import datetime


def dias_vividos(fecha_nacimiento):
    """Calcula los días vividos desde la fecha de nacimiento hasta hoy.

    Args:
        fecha_nacimiento (str): Fecha en formato "YYYY-MM-DD".

    Returns:
        int or None: Número de días vividos o None si el formato es inválido.
    """
    try:
        fecha_nac = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
        hoy = datetime.today()
        return (hoy - fecha_nac).days
    except ValueError:
        return None


def main():
    """Función principal de la aplicación.

    Si se ejecuta en Kubernetes, usa variables de entorno para obtener
    el nombre y la fecha de nacimiento; en local, solicita estos datos al usuario.
    """
    running_in_k8s = os.getenv("RUNNING_IN_K8S", "false").lower() == "true"

    if running_in_k8s:
        nombre = os.getenv("NOMBRE", "Invitado")
        fecha_nacimiento = os.getenv("FECHA_NACIMIENTO", "2000-01-01")
    else:
        try:
            nombre = input("¿Cuál es tu nombre? ")
            fecha_nacimiento = input(
                "¿Cuál es tu fecha de nacimiento? (YYYY-MM-DD): "
            )
        except EOFError:
            print("Error: No se pudo leer la entrada.")
            return

    dias = dias_vividos(fecha_nacimiento)

    if dias is not None:
        print(
            f"Hola, {nombre}! Has vivido aproximadamente {dias} días."
        )
    else:
        print(
            "Error: La fecha ingresada no es válida. "
            "Usa el formato YYYY-MM-DD."
        )


if __name__ == "__main__":
    main()
