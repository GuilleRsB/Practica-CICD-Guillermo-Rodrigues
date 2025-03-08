# Utiliza una imagen oficial de Python
FROM python:3.8-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de dependencias e instala las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY . .

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
