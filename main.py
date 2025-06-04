from src.crypto_analysis import CryptoAnalyzer
import os

def main():
    # Crear directorio para reportes si no existe
    if not os.path.exists('reports'):
        os.makedirs('reports')
    
    # Crear analizador para Bitcoin
    btc_analyzer = CryptoAnalyzer(symbol="BTC")
    
    # Generar datos simulados para el último año
    print("Generando datos simulados para Bitcoin...")
    btc_analyzer.generate_mock_data(days=365)
    
    # Calcular y mostrar métricas
    print("\nMétricas de Bitcoin:")
    metrics = btc_analyzer.calculate_metrics()
    for key, value in metrics.items():
        print(f"{key}: {value:,.2f}")
    
    # Generar reporte completo
    print("\nGenerando reporte completo...")
    btc_analyzer.generate_report()
    
    # Crear analizador para Ethereum
    eth_analyzer = CryptoAnalyzer(symbol="ETH")
    
    # Generar datos simulados para Ethereum
    print("\nGenerando datos simulados para Ethereum...")
    eth_analyzer.generate_mock_data(days=365)
    
    # Calcular y mostrar métricas
    print("\nMétricas de Ethereum:")
    metrics = eth_analyzer.calculate_metrics()
    for key, value in metrics.items():
        print(f"{key}: {value:,.2f}")
    
    # Generar reporte completo
    print("\nGenerando reporte completo...")
    eth_analyzer.generate_report('reports/eth')
    
    print("\n¡Análisis completado! Revisa los reportes en el directorio 'reports'")

if __name__ == "__main__":
    main() 