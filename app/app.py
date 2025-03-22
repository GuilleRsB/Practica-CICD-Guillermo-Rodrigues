from flask import Flask, render_template_string, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Necesario para CSRF

class DatosForm(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired()])
    edad = IntegerField("Edad", validators=[DataRequired()])
    submit = SubmitField("Calcular")

def dias_vividos(edad: int) -> int:
    """
    Calcula la cantidad de días vividos, asumiendo 365 días por año.
    """
    return edad * 365

@app.route("/", methods=["GET", "POST"])
def index():
    form = DatosForm()
    resultado = ""
    if form.validate_on_submit():
        nombre = form.nombre.data
        edad = form.edad.data
        dias = dias_vividos(edad)
        resultado = f"{nombre}, has vivido aproximadamente {dias} días."
    elif request.method == "POST":
        resultado = "Error: Por favor completa todos los campos correctamente."

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
      {{ form.csrf_token }}
      {{ form.nombre.label }} {{ form.nombre(size=20) }}<br><br>
      {{ form.edad.label }} {{ form.edad(min=0) }}<br><br>
      {{ form.submit() }}
    </form>
    <p>{{ resultado }}</p>
  </body>
</html>
        """,
        form=form,
        resultado=resultado,
    )

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
