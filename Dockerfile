# Usa la imagen base de Python 3.8 slim
FROM python:3.8-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requerimientos y luego instálalos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY . .

# Expone el puerto en el que Flask estará escuchando
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
