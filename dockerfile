# Imagen base de Python 3.9
FROM python:3.9-slim-buster

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos de requerimientos
COPY requirements.txt .

# Instalar requerimientos
RUN pip install -r requirements.txt

# Copiar la aplicación
COPY api/ api/
COPY core/ core/
COPY main.py .

# Exponer puerto 8000 para la aplicación
EXPOSE 8000

# Comando para correr la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]