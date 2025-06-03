# Análisis de Regresión - Multivariate Gait Data

Este proyecto realiza un análisis de regresión completo sobre el dataset Multivariate Gait Data de UCI, incluyendo análisis exploratorio de datos, selección de variables y comparación de modelos de regresión.

## Características

- Análisis Exploratorio de Datos (EDA)
  - Boxplots para detección de outliers
  - Matriz de correlación
  - Análisis de Componentes Principales (PCA)
- Selección de variables mediante ganancia de información
- Comparación automática de modelos de regresión usando LazyPredict
- Interfaz web con FastAPI y Jinja2

## Requisitos

- Python 3.9+
- Docker (opcional)

---

## Instalación y Ejecución

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd <nombre-del-directorio>
```

---

### 2. Ejecución en entorno local (sin Docker)

#### a) Crear y activar entorno virtual

```bash
python3.9 -m venv venv
source venv/bin/activate
```

#### b) Instalar dependencias

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### c) Ejecutar la aplicación

```bash
uvicorn app.main:app --reload
```

Luego abre tu navegador en [http://localhost:8000](http://localhost:8000)

---

### 3. Ejecución usando Docker

#### a) Construir la imagen

```bash
docker build -t gait-regresion-app .
```

#### b) Ejecutar el contenedor mapeando el puerto 8000

```bash
docker run -d -p 8000:8000 --name gait-regresion gait-regresion-app
```

- La aplicación estará disponible en [http://localhost:8000](http://localhost:8000)
- Para ver los logs del contenedor:

```bash
docker logs gait-regresion
```

- Para detener y eliminar el contenedor:

```bash
docker stop gait-regresion
docker rm gait-regresion
```

---

### 4. Usar la imagen desde Docker Hub

Puedes descargar y ejecutar la imagen directamente desde Docker Hub:

```bash
docker pull brychxpin/gait-regresion-app:latest
docker run -d -p 8000:8000 --name gait-regresion brychxpin/gait-regresion-app:latest
```

Repositorio oficial en Docker Hub: [https://hub.docker.com/repository/docker/brychxpin/gait-regresion-app/general](https://hub.docker.com/repository/docker/brychxpin/gait-regresion-app/general)

---

## Estructura del Proyecto

```
.
├── app/
│   └── main.py
├── static/
├── templates/
│   └── index.html
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

## Tecnologías Utilizadas

- FastAPI
- Jinja2
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- LazyPredict
- UCI ML Repository API

---

## Notas

- El entorno virtual y archivos temporales están correctamente ignorados en el repositorio.
- El contenedor Docker utiliza Python 3.9 para máxima compatibilidad.
- El dataset se carga automáticamente desde UCI ML Repo.
- Imagen oficial en Docker Hub: [https://hub.docker.com/repository/docker/brychxpin/gait-regresion-app/general](https://hub.docker.com/repository/docker/brychxpin/gait-regresion-app/general)

¿Dudas o problemas? ¡Abre un issue o contacta al autor! 