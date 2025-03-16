from flask import Flask, request, render_template_string

app = Flask(__name__)

def dias_vividos(edad: int) -> int:
    """Calcula la cantidad de días vividos, asumiendo 365 días por año."""
    return edad * 365

# Una plantilla HTML simple
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Días Vividos</title>
</head>
<body>
    <h1>Días Vividos</h1>
    <form method="post">
        <label for="nombre">¿Cuál es tu nombre?</label>
        <input type="text" id="nombre" name="nombre" required><br><br>
        <label for="edad">¿Cuántos años tienes?</label>
        <input type="number" id="edad" name="edad" required><br><br>
        <input type="submit" value="Calcular">
    </form>
    {% if resultado %}
        <h2>{{ nombre }}, has vivido aproximadamente {{ resultado }} días.</h2>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    nombre = ""
    if request.method == "POST":
        nombre = request.form.get("nombre", "Usuario")
        edad_str = request.form.get("edad", "30")
        try:
            edad = int(edad_str)
            resultado = dias_vividos(edad)
        except ValueError:
            resultado = "Error: La edad debe ser un número entero."
    return render_template_string(HTML_TEMPLATE, resultado=resultado, nombre=nombre)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
