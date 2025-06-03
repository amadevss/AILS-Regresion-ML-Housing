from ucimlrepo import fetch_ucirepo
import pandas as pd

def test_dataset():
    try:
        # Cargar dataset
        multivariate_gait_data = fetch_ucirepo(id=760)
        
        # Imprimir información del dataset
        print("Información del dataset:")
        print(f"Nombre: {multivariate_gait_data.metadata.name}")
        
        # Obtener los datos
        X = multivariate_gait_data.data.features
        
        print("\nForma de X:", X.shape)
        print("\nColumnas de X:", X.columns.tolist())
        print("\nPrimeras filas de X:")
        print(X.head())
        
        # Verificar si hay valores nulos
        print("\nValores nulos por columna:")
        print(X.isnull().sum())
        
        # Estadísticas descriptivas
        print("\nEstadísticas descriptivas:")
        print(X.describe())
        
        # Verificar la estructura de los datos
        print("\nTipos de datos:")
        print(X.dtypes)
        
    except Exception as e:
        print(f"Error al cargar el dataset: {str(e)}")

if __name__ == "__main__":
    test_dataset() 