# Selecciona una imagen oficial de Python
FROM python:3.8-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de dependencias y las instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el contenido del repositorio en el contenedor
COPY . .

# Define el comando que se ejecutará al iniciar el contenedor
CMD ["python", "app.py"]
