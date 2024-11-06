#Usa una imagen base de Python
FROM python:3.12-slim

#Ubica el directorio de trabajo en del contenedor
WORKDIR /app

#Copia las dependencias al contenedor
COPY requirements.txt .

#Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

#Copia el contenido al contenedor
COPY . .

#El puerto en el que funcionara la app
EXPOSE 5000

#Configura el entorno para que Flask se ejecute
ENV FLASK_ENV=production

#Comando para ejecutar la aplicación
CMD ["python", "app.py"]