# gait-regresion-app

Imagen Docker para el análisis de regresión sobre el dataset Multivariate Gait Data de UCI.

## ¿Qué hace esta imagen?
- Ejecuta una API web con FastAPI para análisis exploratorio, selección de variables y comparación de modelos de regresión.
- Incluye visualizaciones y tablas interactivas accesibles desde el navegador.

## Uso rápido

### Descargar la imagen
```bash
docker pull brychxpin/gait-regresion-app:latest
```

### Ejecutar el contenedor
```bash
docker run -d -p 8000:8000 --name gait-regresion brychxpin/gait-regresion-app:latest
```

Luego abre tu navegador en [http://localhost:8000](http://localhost:8000)

## Variables de entorno
No requiere configuración adicional.

## Actualizaciones
La imagen se actualizará con mejoras y correcciones. Puedes obtener la última versión con:
```bash
docker pull brychxpin/gait-regresion-app:latest
```

## Código fuente
El código fuente está disponible en el repositorio principal de GitHub.

---

¿Dudas o problemas? Abre un issue en el repositorio o contacta al autor vía Docker Hub. 