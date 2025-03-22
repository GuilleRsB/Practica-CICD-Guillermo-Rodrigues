# Usa la imagen base de Python 3.8 slim cambiada a alpine por tener menos vulnerabilidades
FROM python:3.14-rc-alpine3.21

# Establece el directorio de trabajo
WORKDIR app.py /app/

# Copia los archivos de requerimientos y luego instálalos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY . .

# Expone el puerto en el que Flask estará escuchando
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
