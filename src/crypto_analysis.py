# Importaciones necesarias para el análisis de criptomonedas
import pandas as pd          # Para manejo de datos tabulares y análisis
import numpy as np          # Para cálculos numéricos y generación de datos aleatorios
from datetime import datetime, timedelta  # Para manejo de fechas y períodos
import matplotlib.pyplot as plt  # Para creación de gráficos básicos
import seaborn as sns      # Para visualizaciones estadísticas avanzadas
from typing import Dict, List, Optional, Union  # Para tipado estático y documentación

class CryptoAnalyzer:
    """
    Clase principal para el análisis de criptomonedas.
    Permite generar datos simulados, calcular métricas y crear visualizaciones.
    """
    
    def __init__(self, symbol: str = "BTC"):
        """
        Inicializa el analizador de criptomonedas.
        
        Args:
            symbol (str): Símbolo de la criptomoneda (por defecto "BTC")
        """
        self.symbol = symbol  # Guarda el símbolo de la criptomoneda
        self.data = None      # Inicializa el DataFrame de datos como None
        
    def generate_mock_data(self, days: int = 365) -> pd.DataFrame:
        """
        Genera datos simulados de una criptomoneda para análisis.
        Los datos incluyen precios, volumen y capitalización de mercado.
        
        Args:
            days (int): Número de días de datos a generar
            
        Returns:
            pd.DataFrame: DataFrame con datos simulados
        """
        # Generar rango de fechas desde hoy hacia atrás
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        dates = pd.date_range(start=start_date, end=end_date, freq='D')
        
        # Configuración de precios base
        base_price = 20000  # Precio inicial de la criptomoneda
        
        # Generar tendencia alcista usando linspace
        # Crea una secuencia de números que va de 0 a 10000
        trend = np.linspace(0, 10000, len(dates))
        
        # Generar volatilidad usando distribución normal
        # Media = 0, Desviación estándar = 1000
        volatility = np.random.normal(0, 1000, len(dates))
        
        # Calcular precios finales combinando:
        # - Precio base
        # - Tendencia alcista
        # - Volatilidad aleatoria
        prices = base_price + trend + volatility
        
        # Generar volumen de trading usando distribución log-normal
        # Esto asegura que el volumen siempre sea positivo
        volume = np.random.lognormal(10, 1, len(dates))
        
        # Calcular métricas adicionales
        market_cap = prices * volume * 1000  # Capitalización de mercado simulada
        trading_volume = volume * prices     # Volumen de trading en USD
        
        # Crear DataFrame con todos los datos
        self.data = pd.DataFrame({
            'fecha': dates,           # Fechas
            'precio': prices,         # Precios
            'volumen': volume,        # Volumen base
            'market_cap': market_cap, # Capitalización de mercado
            'trading_volume': trading_volume  # Volumen de trading
        })
        
        return self.data
    
    def calculate_metrics(self) -> Dict:
        """
        Calcula métricas importantes de la criptomoneda.
        Incluye precios, volatilidad, retornos y capitalización.
        
        Returns:
            Dict: Diccionario con métricas calculadas
        """
        # Verificar que existan datos
        if self.data is None:
            raise ValueError("Primero debes generar o cargar datos")
            
        # Calcular métricas clave
        metrics = {
            'precio_actual': self.data['precio'].iloc[-1],  # Último precio
            'precio_maximo': self.data['precio'].max(),     # Precio más alto
            'precio_minimo': self.data['precio'].min(),     # Precio más bajo
            'volumen_promedio': self.data['volumen'].mean(), # Volumen promedio
            'volatilidad': self.data['precio'].std(),       # Desviación estándar
            'retorno_total': (self.data['precio'].iloc[-1] / self.data['precio'].iloc[0] - 1) * 100,  # Retorno porcentual
            'market_cap_actual': self.data['market_cap'].iloc[-1]  # Capitalización actual
        }
        
        return metrics
    
    def plot_price_history(self, save_path: Optional[str] = None):
        """
        Genera un gráfico del historial de precios.
        Muestra la evolución del precio a lo largo del tiempo.
        
        Args:
            save_path (Optional[str]): Ruta para guardar el gráfico
        """
        plt.figure(figsize=(12, 6))  # Tamaño del gráfico
        plt.plot(self.data['fecha'], self.data['precio'])  # Gráfico de línea
        plt.title(f'Historial de Precios - {self.symbol}')
        plt.xlabel('Fecha')
        plt.ylabel('Precio (USD)')
        plt.grid(True)  # Agregar cuadrícula
        
        # Guardar gráfico si se especifica ruta
        if save_path:
            plt.savefig(save_path)
        plt.show()
    
    def plot_volume(self, save_path: Optional[str] = None):
        """
        Genera un gráfico del volumen de trading.
        Muestra el volumen de operaciones a lo largo del tiempo.
        
        Args:
            save_path (Optional[str]): Ruta para guardar el gráfico
        """
        plt.figure(figsize=(12, 6))
        plt.bar(self.data['fecha'], self.data['trading_volume'])  # Gráfico de barras
        plt.title(f'Volumen de Trading - {self.symbol}')
        plt.xlabel('Fecha')
        plt.ylabel('Volumen (USD)')
        plt.grid(True)
        
        if save_path:
            plt.savefig(save_path)
        plt.show()
    
    def plot_price_distribution(self, save_path: Optional[str] = None):
        """
        Genera un gráfico de la distribución de precios.
        Muestra la distribución estadística de los precios.
        
        Args:
            save_path (Optional[str]): Ruta para guardar el gráfico
        """
        plt.figure(figsize=(10, 6))
        # Histograma con curva de densidad
        sns.histplot(self.data['precio'], kde=True)
        plt.title(f'Distribución de Precios - {self.symbol}')
        plt.xlabel('Precio (USD)')
        plt.ylabel('Frecuencia')
        
        if save_path:
            plt.savefig(save_path)
        plt.show()
    
    def plot_market_cap(self, save_path: Optional[str] = None):
        """
        Genera un gráfico de la capitalización de mercado.
        Muestra la evolución de la capitalización a lo largo del tiempo.
        
        Args:
            save_path (Optional[str]): Ruta para guardar el gráfico
        """
        plt.figure(figsize=(12, 6))
        plt.plot(self.data['fecha'], self.data['market_cap'])
        plt.title(f'Capitalización de Mercado - {self.symbol}')
        plt.xlabel('Fecha')
        plt.ylabel('Market Cap (USD)')
        plt.grid(True)
        
        if save_path:
            plt.savefig(save_path)
        plt.show()
    
    def generate_report(self, output_dir: str = 'reports'):
        """
        Genera un reporte completo con gráficos y métricas.
        Crea un directorio con todos los análisis y visualizaciones.
        
        Args:
            output_dir (str): Directorio para guardar los reportes
        """
        import os
        # Crear directorio si no existe
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        # Calcular métricas
        metrics = self.calculate_metrics()
        
        # Generar y guardar todos los gráficos
        self.plot_price_history(f'{output_dir}/price_history.png')
        self.plot_volume(f'{output_dir}/volume.png')
        self.plot_price_distribution(f'{output_dir}/price_distribution.png')
        self.plot_market_cap(f'{output_dir}/market_cap.png')
        
        # Guardar métricas en un archivo de texto
        with open(f'{output_dir}/metrics.txt', 'w') as f:
            f.write(f"Reporte de Análisis - {self.symbol}\n")
            f.write("=" * 50 + "\n\n")
            for key, value in metrics.items():
                f.write(f"{key}: {value:,.2f}\n")
        
        print(f"Reporte generado en el directorio: {output_dir}") 