from flask import Flask, request, render_template_string

app = Flask(__name__)

# CSRF protection no se usa porque esta app no modifica datos críticos ni mantiene sesión.
# La validación de entrada está controlada manualmente.
# Esto es aceptable para fines educativos y aplicaciones simples sin usuarios autenticados.


def dias_vividos(edad: int) -> int:
    """
    Calcula la cantidad de días vividos, asumiendo 365 días por año.

    Args:
        edad (int): La edad en años.

    Returns:
        int: El número aproximado de días vividos.
    """
    return edad * 365


# Esta ruta permite GET y POST de forma controlada.
# No se modifica el estado del servidor ni se almacenan datos sensibles.
@app.route("/", methods=["GET", "POST"])
def index():
    resultado = ""
    if request.method == "POST":
        nombre = request.form.get("nombre", "Usuario")
        edad_str = request.form.get("edad", "30")
        try:
            edad = int(edad_str)
            dias = dias_vividos(edad)
            resultado = (
                f"{nombre}, has vivido aproximadamente {dias} días."
            )
        except ValueError:
            resultado = "Error: La edad debe ser un número entero."
    return render_template_string(
        """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Días Vividos</title>
  </head>
  <body>
    <h1>Calcula los días vividos</h1>
    <form method="post">
      <label for="nombre">Nombre:</label>
      <input type="text" name="nombre" id="nombre" required><br><br>
      <label for="edad">Edad:</label>
      <input type="number" name="edad" id="edad" required><br><br>
      <input type="submit" value="Calcular">
    </form>
    <p>{{ resultado }}</p>
  </body>
</html>
        """,
        resultado=resultado,
    )


if __name__ == '__main__':
    # Escucha en todas las interfaces solo si estás en producción (Docker/Kubernetes)
    host = "0.0.0.0" if os.getenv("FLASK_ENV") == "production" else "127.0.0.1"
    app.run(host=host, port=5000)
