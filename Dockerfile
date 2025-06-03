# Usar una imagen base ligera de Python 3.9
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema necesarias
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copiar los archivos de requisitos primero para aprovechar la caché de Docker
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Crear directorios necesarios
RUN mkdir -p app/static templates

# Copiar el resto de la aplicación
COPY app/ app/
COPY templates/ templates/
COPY static/ app/static/

# Exponer el puerto que usará la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"] 