# Creamos el Dockerfile con las instrucciones necesarias para crear la imagen
# Deriving the latest base image
FROM python:latest

# Introducimos las etiquetas como pares clave-valor
LABEL Maintainer="Adrianrobarq"

# Creamos un entorno de trabajo
ENV PYTHONPATH=/usr/app/src

# Especificamos un directorio de trabajo
WORKDIR /usr/app/src

#  Creamos un directorio para almacenar los archivos de imagen
RUN mkdir -p /usr/app/src/images

# Exportamos las imágenes a un directorio local
VOLUME ./app_images/:/usr/app/src/images

# Copiamos el archivo de prueba al contenedor
COPY dependencies_test.py .

# Copiamos el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instalamos las dependencias necesarias
RUN pip install -r requirements.txt

# Creamos el CMD para ejecutar el script de prueba
CMD [ "python", "./dependencies_test.py"]