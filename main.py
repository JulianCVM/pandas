# Importar la clase CryptoAnalyzer del módulo crypto_analysis
from src.crypto_analysis import CryptoAnalyzer
import os  # Para manejo de directorios y rutas

def main():
    """
    Función principal que ejecuta el análisis de criptomonedas.
    Analiza Bitcoin y Ethereum, generando reportes para cada uno.
    """
    # Crear directorio para reportes si no existe
    if not os.path.exists('reports'):
        os.makedirs('reports')
    
    # Análisis de Bitcoin
    print("\n=== Análisis de Bitcoin ===")
    # Crear instancia del analizador para Bitcoin
    btc_analyzer = CryptoAnalyzer(symbol="BTC")
    # Generar datos simulados para el último año
    btc_analyzer.generate_mock_data(days=365)
    
    # Calcular y mostrar métricas de Bitcoin
    btc_metrics = btc_analyzer.calculate_metrics()
    print("\nMétricas de Bitcoin:")
    for key, value in btc_metrics.items():
        print(f"{key}: {value:,.2f}")
    
    # Generar reporte completo de Bitcoin
    btc_analyzer.generate_report(output_dir='reports/btc')
    
    # Análisis de Ethereum
    print("\n=== Análisis de Ethereum ===")
    # Crear instancia del analizador para Ethereum
    eth_analyzer = CryptoAnalyzer(symbol="ETH")
    # Generar datos simulados para Ethereum
    eth_analyzer.generate_mock_data(days=365)
    
    # Calcular y mostrar métricas de Ethereum
    eth_metrics = eth_analyzer.calculate_metrics()
    print("\nMétricas de Ethereum:")
    for key, value in eth_metrics.items():
        print(f"{key}: {value:,.2f}")
    
    # Generar reporte completo de Ethereum
    eth_analyzer.generate_report(output_dir='reports/eth')
    
    print("\nAnálisis completado. Revisa los reportes en el directorio 'reports'")

# Punto de entrada del programa
if __name__ == "__main__":
    main() 