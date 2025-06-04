import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, List, Optional, Union

class CryptoAnalyzer:
    def __init__(self, symbol: str = "BTC"):
        """
        Inicializa el analizador de criptomonedas.
        
        Args:
            symbol (str): Símbolo de la criptomoneda (por defecto "BTC")
        """
        self.symbol = symbol
        self.data = None
        
    def generate_mock_data(self, days: int = 365) -> pd.DataFrame:
        """
        Genera datos simulados de una criptomoneda.
        
        Args:
            days (int): Número de días de datos a generar
            
        Returns:
            pd.DataFrame: DataFrame con datos simulados
        """
        # Generar fechas
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        dates = pd.date_range(start=start_date, end=end_date, freq='D')
        
        # Generar precios base con tendencia alcista
        base_price = 20000  # Precio inicial
        trend = np.linspace(0, 10000, len(dates))  # Tendencia alcista
        volatility = np.random.normal(0, 1000, len(dates))  # Volatilidad
        
        # Calcular precios
        prices = base_price + trend + volatility
        
        # Generar volumen
        volume = np.random.lognormal(10, 1, len(dates))
        
        # Generar métricas adicionales
        market_cap = prices * volume * 1000  # Capitalización de mercado simulada
        trading_volume = volume * prices  # Volumen de trading
        
        # Crear DataFrame
        self.data = pd.DataFrame({
            'fecha': dates,
            'precio': prices,
            'volumen': volume,
            'market_cap': market_cap,
            'trading_volume': trading_volume
        })
        
        return self.data
    
    def calculate_metrics(self) -> Dict:
        """
        Calcula métricas importantes de la criptomoneda.
        
        Returns:
            Dict: Diccionario con métricas calculadas
        """
        if self.data is None:
            raise ValueError("Primero debes generar o cargar datos")
            
        metrics = {
            'precio_actual': self.data['precio'].iloc[-1],
            'precio_maximo': self.data['precio'].max(),
            'precio_minimo': self.data['precio'].min(),
            'volumen_promedio': self.data['volumen'].mean(),
            'volatilidad': self.data['precio'].std(),
            'retorno_total': (self.data['precio'].iloc[-1] / self.data['precio'].iloc[0] - 1) * 100,
            'market_cap_actual': self.data['market_cap'].iloc[-1]
        }
        
        return metrics
    
    def plot_price_history(self, save_path: Optional[str] = None):
        """
        Genera un gráfico del historial de precios.
        
        Args:
            save_path (Optional[str]): Ruta para guardar el gráfico
        """
        plt.figure(figsize=(12, 6))
        plt.plot(self.data['fecha'], self.data['precio'])
        plt.title(f'Historial de Precios - {self.symbol}')
        plt.xlabel('Fecha')
        plt.ylabel('Precio (USD)')
        plt.grid(True)
        
        if save_path:
            plt.savefig(save_path)
        plt.show()
    
    def plot_volume(self, save_path: Optional[str] = None):
        """
        Genera un gráfico del volumen de trading.
        
        Args:
            save_path (Optional[str]): Ruta para guardar el gráfico
        """
        plt.figure(figsize=(12, 6))
        plt.bar(self.data['fecha'], self.data['trading_volume'])
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
        
        Args:
            save_path (Optional[str]): Ruta para guardar el gráfico
        """
        plt.figure(figsize=(10, 6))
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
        
        Args:
            output_dir (str): Directorio para guardar los reportes
        """
        import os
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        # Calcular métricas
        metrics = self.calculate_metrics()
        
        # Generar gráficos
        self.plot_price_history(f'{output_dir}/price_history.png')
        self.plot_volume(f'{output_dir}/volume.png')
        self.plot_price_distribution(f'{output_dir}/price_distribution.png')
        self.plot_market_cap(f'{output_dir}/market_cap.png')
        
        # Guardar métricas en un archivo
        with open(f'{output_dir}/metrics.txt', 'w') as f:
            f.write(f"Reporte de Análisis - {self.symbol}\n")
            f.write("=" * 50 + "\n\n")
            for key, value in metrics.items():
                f.write(f"{key}: {value:,.2f}\n")
        
        print(f"Reporte generado en el directorio: {output_dir}") 