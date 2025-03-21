from flask import Flask, request, render_template_string

app = Flask(__name__)

def dias_vividos(edad: int) -> int:
    """
    Calcula la cantidad de días vividos, asumiendo 365 días por año.

    Args:
        edad (int): La edad en años.

    Returns:
        int: El número aproximado de días vividos.
    """
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")
    return edad * 365

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = ""
    if request.method == "POST":
        nombre = request.form.get("nombre", "Usuario")
        edad_str = request.form.get("edad", "30")
        try:
            edad = int(edad_str)
            dias = dias_vividos(edad)
            resultado = f"{nombre}, has vivido aproximadamente {dias:,} días."
        except ValueError:
            resultado = "❌ Error: La edad debe ser un número entero y no negativa."

    html = """
    <!DOCTYPE html>
    <html lang="es">
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
    """
    return render_template_string(html, resultado=resultado)

def main():
    """Función principal de entrada."""
    app.run(host="0.0.0.0", port=5000)

if __name__ == '__main__':
    main()
