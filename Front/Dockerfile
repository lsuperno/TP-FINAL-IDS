# Imagen base de Python
FROM python:3.11

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia todos los archivos de tu proyecto
COPY . /app

# Instala las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 8080 (donde Flask va a correr)
EXPOSE 8080

# Comando para iniciar la app
CMD ["python", "app.py"]
