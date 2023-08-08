# Idicar la version de python para la imagen que se creará
FROM python:3.10.11

# Congigurar el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los directorios del proyecto a director de trabajo de contenedor
COPY . .

# Instalacion de los paquetes necesarios
RUN pip install --no-cache-dir -r requirements.txt

# Definir el puerto que se usará para correr la aplicacion
EXPOSE 83

# Definir en comando para correr la aplicacion
CMD ["python", "manage.py", "runserver", "172.17.0.2:83"]

# docker inspect network bridge
