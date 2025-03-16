import os
import time

def dias_vividos(edad: int) -> int:
    """
    Calcula la cantidad de días vividos, asumiendo 365 días por año.
    """
    return edad * 365

def main():
    """
    Función principal que obtiene los valores desde variables de entorno.
    """
    print("Iniciando la aplicación CLI...", flush=True)

    nombre = os.getenv("NOMBRE", "Usuario")
    edad_str = os.getenv("EDAD", "30")

    try:
        edad = int(edad_str)
    except ValueError:
        print("Error: La edad debe ser un número entero.", flush=True)
        return

    dias = dias_vividos(edad)
    print(f"{nombre}, has vivido aproximadamente {dias} días.", flush=True)

    # Mantener la aplicación en ejecución para evitar que el contenedor termine
    while True:
        time.sleep(3600)  # Espera 1 hora antes de volver a iterar

if __name__ == '__main__':
    main()
