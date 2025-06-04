import pandas as pd
import numpy as np
from typing import Union, List, Dict
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_clean_data(file_path: str) -> pd.DataFrame:
    """
    Carga y limpia los datos de un archivo CSV.
    
    Args:
        file_path (str): Ruta al archivo CSV
        
    Returns:
        pd.DataFrame: DataFrame limpio
    """
    try:
        df = pd.read_csv(file_path)
        # Eliminar filas duplicadas
        df = df.drop_duplicates()
        # Eliminar filas con valores nulos
        df = df.dropna()
        return df
    except Exception as e:
        print(f"Error al cargar los datos: {str(e)}")
        return pd.DataFrame()

def get_basic_stats(df: pd.DataFrame) -> Dict:
    """
    Obtiene estadísticas básicas del DataFrame.
    
    Args:
        df (pd.DataFrame): DataFrame a analizar
        
    Returns:
        Dict: Diccionario con estadísticas básicas
    """
    stats = {
        'shape': df.shape,
        'columns': df.columns.tolist(),
        'dtypes': df.dtypes.to_dict(),
        'missing_values': df.isnull().sum().to_dict(),
        'numeric_stats': df.describe().to_dict()
    }
    return stats

def analyze_correlations(df: pd.DataFrame, method: str = 'pearson') -> pd.DataFrame:
    """
    Analiza las correlaciones entre variables numéricas.
    
    Args:
        df (pd.DataFrame): DataFrame a analizar
        method (str): Método de correlación ('pearson', 'kendall', 'spearman')
        
    Returns:
        pd.DataFrame: Matriz de correlaciones
    """
    numeric_df = df.select_dtypes(include=[np.number])
    return numeric_df.corr(method=method)

def plot_correlation_heatmap(df: pd.DataFrame, method: str = 'pearson') -> None:
    """
    Genera un mapa de calor de correlaciones.
    
    Args:
        df (pd.DataFrame): DataFrame a analizar
        method (str): Método de correlación
    """
    corr = analyze_correlations(df, method)
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
    plt.title('Matriz de Correlaciones')
    plt.tight_layout()
    plt.show()

def group_and_aggregate(df: pd.DataFrame, 
                       group_by: Union[str, List[str]], 
                       agg_dict: Dict) -> pd.DataFrame:
    """
    Agrupa y agrega datos según criterios específicos.
    
    Args:
        df (pd.DataFrame): DataFrame a analizar
        group_by (Union[str, List[str]]): Columna(s) para agrupar
        agg_dict (Dict): Diccionario de funciones de agregación
        
    Returns:
        pd.DataFrame: DataFrame agrupado
    """
    return df.groupby(group_by).agg(agg_dict)

def filter_data(df: pd.DataFrame, 
                conditions: Dict[str, Union[str, int, float]]) -> pd.DataFrame:
    """
    Filtra el DataFrame según condiciones específicas.
    
    Args:
        df (pd.DataFrame): DataFrame a filtrar
        conditions (Dict): Diccionario de condiciones
        
    Returns:
        pd.DataFrame: DataFrame filtrado
    """
    mask = pd.Series(True, index=df.index)
    for column, value in conditions.items():
        mask &= (df[column] == value)
    return df[mask]

if __name__ == "__main__":
    # Ejemplo de uso
    print("Módulo de análisis de datos cargado correctamente.") 