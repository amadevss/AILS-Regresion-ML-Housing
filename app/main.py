from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import mutual_info_regression
from lazypredict.Supervised import LazyRegressor
from sklearn.model_selection import train_test_split
import base64
from io import BytesIO
from ucimlrepo import fetch_ucirepo

app = FastAPI()

# Montar archivos estáticos y templates
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="templates")

def fig_to_base64(fig):
    buf = BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    return base64.b64encode(buf.getvalue()).decode()

@app.get("/")
async def home(request: Request):
    try:
        # Cargar dataset
        multivariate_gait_data = fetch_ucirepo(id=760)
        data = multivariate_gait_data.data.features

        # Muestreo aleatorio para acelerar el análisis
        data_sample = data.sample(n=3000, random_state=42)

        # Separar características y objetivo
        X = data_sample.drop('angle', axis=1)
        y = data_sample['angle']

        # EDA - Boxplots
        plt.figure(figsize=(12, 6))
        sns.boxplot(data=X)
        plt.xticks(rotation=45)
        plt.title('Boxplots de Variables')
        boxplot_img = fig_to_base64(plt.gcf())
        plt.close()

        # Matriz de correlación
        plt.figure(figsize=(10, 8))
        sns.heatmap(X.corr(), annot=True, cmap='coolwarm')
        plt.title('Matriz de Correlación')
        corr_img = fig_to_base64(plt.gcf())
        plt.close()

        # PCA
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        pca = PCA()
        pca.fit(X_scaled)
        
        plt.figure(figsize=(10, 6))
        plt.plot(range(1, len(pca.explained_variance_ratio_) + 1),
                 np.cumsum(pca.explained_variance_ratio_), 'bo-')
        plt.xlabel('Número de Componentes')
        plt.ylabel('Varianza Explicada Acumulada')
        plt.title('Varianza Explicada por PCA')
        pca_img = fig_to_base64(plt.gcf())
        plt.close()

        # Ganancia de información
        mi_scores = mutual_info_regression(X, y)
        mi_df = pd.DataFrame({
            'Variable': X.columns,
            'Ganancia de Información': mi_scores
        }).sort_values('Ganancia de Información', ascending=False)

        # LazyPredict
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        reg = LazyRegressor(verbose=0, ignore_warnings=True, custom_metric=None)
        models, predictions = reg.fit(X_train, X_test, y_train, y_test)
        
        # Convertir resultados a formato HTML
        mi_table = mi_df.to_html(classes='table table-striped', index=False)
        models_table = models.to_html(classes='table table-striped')

        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "boxplot_img": boxplot_img,
                "corr_img": corr_img,
                "pca_img": pca_img,
                "mi_table": mi_table,
                "models_table": models_table
            }
        )
    except Exception as e:
        # En caso de error, mostrar una página de error
        return templates.TemplateResponse(
            "error.html",
            {
                "request": request,
                "error_message": str(e)
            }
        )
