import os
from datetime import datetime

def calcular_dias_vividos(fecha_nacimiento):
    """ Calcula los días vividos desde la fecha de nacimiento hasta hoy. """
    try:
        fecha_nac = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")  # Formato YYYY-MM-DD
        hoy = datetime.today()
        dias_vividos = (hoy - fecha_nac).days
        return dias_vividos
    except ValueError:
        return None  # Si el formato de la fecha es incorrecto

def main():
    # Detectar si la app está corriendo en Kubernetes o en local
    running_in_k8s = os.getenv("RUNNING_IN_K8S", "false").lower() == "true"

    if running_in_k8s:
        nombre = os.getenv("NOMBRE", "Invitado")  # Nombre desde variable de entorno
        fecha_nacimiento = os.getenv("FECHA_NACIMIENTO", "2000-01-01")  # Fecha desde variable de entorno
    else:
        nombre = input("¿Cuál es tu nombre? ")  # Pregunta solo si está en local
        fecha_nacimiento = input("¿Cuál es tu fecha de nacimiento? (YYYY-MM-DD): ")

    dias_vividos = calcular_dias_vividos(fecha_nacimiento)

    if dias_vividos is not None:
        print(f"Hola, {nombre}! Has vivido aproximadamente {dias_vividos} días.")
    else:
        print("Error: La fecha de nacimiento ingresada no es válida. Usa el formato YYYY-MM-DD.")

if __name__ == "__main__":
    main()
