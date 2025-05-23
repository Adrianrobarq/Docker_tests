# Creamos el Dockerfile con las instrucciones necesarias para crear la imagen
# Deriving the latest base image
FROM python:latest

# Introducimos las etiquetas como pares clave-valor
LABEL Maintainer="Adrianrobarq"

# Especificamos un directorio de trabajo
WORKDIR /usr/app/src

# Copiamos el archivo de prueba al contenedor
COPY dependencies_test.py .

# Copiamos el archivo requirements.txt al contenedor
COPY dependencies.txt .

# Instalamos las dependencias necesarias
RUN pip install -r dependencies.txt

# Creamos el CMD para ejecutar el script de prueba
CMD [ "python", "./dependencies_test.py"]