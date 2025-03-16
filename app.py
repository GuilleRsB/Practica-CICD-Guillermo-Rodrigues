from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

def dias_vividos(edad: int) -> int:
    """
    Calcula la cantidad de días vividos, asumiendo 365 días por año.
    """
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
            resultado = f"{nombre}, has vivido aproximadamente {dias} días."
        except ValueError:
            resultado = "Error: La edad debe ser un número entero."
    return render_template_string("""
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
    """, resultado=resultado)

if __name__ == '__main__':
    # Escucha en todas las interfaces, puerto 5000
    app.run(host="0.0.0.0", port=5000)
