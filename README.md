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

## Instalación

### Usando pip

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd <nombre-del-directorio>
```

2. Crear un entorno virtual (opcional pero recomendado):
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

### Usando Docker

1. Construir la imagen:
```bash
docker build -t gait-analysis .
```

2. Ejecutar el contenedor:
```bash
docker run -p 8000:8000 gait-analysis
```

## Uso

1. Iniciar el servidor:
```bash
uvicorn app.main:app --reload
```

2. Abrir el navegador en `http://localhost:8000`

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