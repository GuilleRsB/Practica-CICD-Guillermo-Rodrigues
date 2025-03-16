from flask import Flask, request, render_template_string

app = Flask(__name__)

def dias_vividos(edad: int) -> int:
    """
    Calcula la cantidad de días vividos, asumiendo 365 días por año.
    """
    return edad * 365

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.form.get('nombre', 'Usuario')
        edad_str = request.form.get('edad', '30')
        try:
            edad = int(edad_str)
        except ValueError:
            return render_template_string('''
                <!doctype html>
                <html>
                <head><title>Error</title></head>
                <body>
                    <p>Error: La edad debe ser un número entero.</p>
                    <a href="/">Volver</a>
                </body>
                </html>
            '''), 400

        dias = dias_vividos(edad)
        mensaje = f"{nombre}, has vivido aproximadamente {dias} días."
        return render_template_string('''
            <!doctype html>
            <html>
            <head>
                <title>Resultado</title>
            </head>
            <body>
                <h2>Resultado</h2>
                <p>{{ mensaje }}</p>
                <a href="/">Volver</a>
            </body>
            </html>
        ''', mensaje=mensaje)
    else:
        # Mostrar el formulario
        return render_template_string('''
            <!doctype html>
            <html>
            <head>
                <title>Calculadora de Días Vividos</title>
            </head>
            <body>
                <h1>Calculadora de Días Vividos</h1>
                <form method="post">
                    <label for="nombre">Nombre:</label><br>
                    <input type="text" id="nombre" name="nombre" placeholder="Ingresa tu nombre"><br><br>
                    <label for="edad">Edad:</label><br>
                    <input type="number" id="edad" name="edad" placeholder="Ingresa tu edad"><br><br>
                    <input type="submit" value="Calcular">
                </form>
            </body>
            </html>
        ''')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
