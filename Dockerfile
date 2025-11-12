# --- ETAPA 1: CONSTRUIR EL FRONTEND (Vite) ---
# Usamos una imagen de Node para compilar el React
FROM node:18-alpine AS frontend-builder

# Vamos a laburar en la carpeta /app-front
WORKDIR /app-front

# Copiamos los package.json (para cachear dependencias)
COPY frontend/package.json frontend/package-lock.json* ./
RUN npm install

# Copiamos el resto del código del front y lo compilamos
COPY frontend/ ./
RUN npm run build
# Esto nos deja la carpeta /app-front/dist lista para usar

# --- ETAPA 2: CONSTRUIR EL BACKEND Y JUNTAR TODO ---
# Empezamos de cero con la imagen de Python
FROM python:3.11-slim

# Seteamos el directorio de laburo
WORKDIR /app

# Copiamos e instalamos las dependencias del back
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el código del backend
COPY backend/ .

# === ¡LA MAGIA! ===
# Copiamos los archivos compilados del front (de la Etapa 1)
# adentro de una carpeta 'static' en nuestro backend.
COPY --from=frontend-builder /app-front/dist ./static

# Exponemos el puerto que usa FastAPI
EXPOSE 8000

# El 'app:app' funciona porque copiamos 'backend/' a '.' 
# y nuestro WORKDIR es /app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
