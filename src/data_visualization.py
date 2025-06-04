import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Optional, Union
import numpy as np

def set_style():
    """
    Configura el estilo de las visualizaciones.
    """
    plt.style.use('seaborn')
    sns.set_palette("husl")

def plot_numeric_distribution(df: pd.DataFrame, 
                            column: str, 
                            bins: int = 30) -> None:
    """
    Genera un histograma con curva de densidad para una variable numérica.
    
    Args:
        df (pd.DataFrame): DataFrame con los datos
        column (str): Nombre de la columna a visualizar
        bins (int): Número de bins para el histograma
    """
    set_style()
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x=column, bins=bins, kde=True)
    plt.title(f'Distribución de {column}')
    plt.xlabel(column)
    plt.ylabel('Frecuencia')
    plt.show()

def plot_categorical_counts(df: pd.DataFrame, 
                          column: str, 
                          top_n: Optional[int] = None) -> None:
    """
    Genera un gráfico de barras para variables categóricas.
    
    Args:
        df (pd.DataFrame): DataFrame con los datos
        column (str): Nombre de la columna categórica
        top_n (Optional[int]): Número de categorías a mostrar
    """
    set_style()
    plt.figure(figsize=(12, 6))
    value_counts = df[column].value_counts()
    if top_n:
        value_counts = value_counts.head(top_n)
    sns.barplot(x=value_counts.index, y=value_counts.values)
    plt.title(f'Conteo de {column}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_scatter_matrix(df: pd.DataFrame, 
                       columns: List[str], 
                       hue: Optional[str] = None) -> None:
    """
    Genera una matriz de gráficos de dispersión.
    
    Args:
        df (pd.DataFrame): DataFrame con los datos
        columns (List[str]): Lista de columnas a visualizar
        hue (Optional[str]): Columna para colorear los puntos
    """
    set_style()
    sns.pairplot(df[columns], hue=hue)
    plt.show()

def plot_time_series(df: pd.DataFrame, 
                    date_column: str, 
                    value_column: str, 
                    freq: str = 'D') -> None:
    """
    Genera un gráfico de series temporales.
    
    Args:
        df (pd.DataFrame): DataFrame con los datos
        date_column (str): Columna de fechas
        value_column (str): Columna de valores
        freq (str): Frecuencia de agregación ('D' para diario, 'M' para mensual, etc.)
    """
    set_style()
    df[date_column] = pd.to_datetime(df[date_column])
    time_series = df.set_index(date_column)[value_column].resample(freq).mean()
    
    plt.figure(figsize=(12, 6))
    time_series.plot()
    plt.title(f'Serie Temporal de {value_column}')
    plt.xlabel('Fecha')
    plt.ylabel(value_column)
    plt.grid(True)
    plt.show()

def plot_boxplot(df: pd.DataFrame, 
                x: str, 
                y: str, 
                hue: Optional[str] = None) -> None:
    """
    Genera un gráfico de cajas (boxplot).
    
    Args:
        df (pd.DataFrame): DataFrame con los datos
        x (str): Columna para el eje x
        y (str): Columna para el eje y
        hue (Optional[str]): Columna para separar los grupos
    """
    set_style()
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x=x, y=y, hue=hue)
    plt.title(f'Boxplot de {y} por {x}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_heatmap(df: pd.DataFrame, 
                columns: Optional[List[str]] = None) -> None:
    """
    Genera un mapa de calor de correlaciones.
    
    Args:
        df (pd.DataFrame): DataFrame con los datos
        columns (Optional[List[str]]): Lista de columnas a incluir
    """
    set_style()
    if columns:
        corr_matrix = df[columns].corr()
    else:
        corr_matrix = df.corr()
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title('Matriz de Correlaciones')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("Módulo de visualización cargado correctamente.") 