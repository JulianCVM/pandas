# Análisis de Criptomonedas con Pandas

Este proyecto proporciona herramientas para analizar datos de criptomonedas, generando datos simulados y realizando análisis técnico y visualización.

## Estructura del Proyecto

```
.
├── README.md
├── requirements.txt
├── main.py              # Script principal
├── src/
│   ├── __init__.py
│   └── crypto_analysis.py    # Módulo de análisis de criptomonedas
└── reports/             # Directorio para reportes generados
    ├── btc/            # Reportes de Bitcoin
    └── eth/            # Reportes de Ethereum
```

## Requisitos

Para ejecutar este proyecto, necesitas tener instalado:

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. Clona este repositorio:
```bash
git clone [URL_DEL_REPOSITORIO]
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

### Ejecución Rápida

Para ejecutar el análisis completo:

```bash
python main.py
```

Esto generará:
- Datos simulados para Bitcoin y Ethereum
- Métricas clave para cada criptomoneda
- Gráficos y visualizaciones
- Reportes completos en el directorio `reports`

### Uso del Módulo de Análisis

```python
from src.crypto_analysis import CryptoAnalyzer

# Crear analizador para una criptomoneda
analyzer = CryptoAnalyzer(symbol="BTC")

# Generar datos simulados
analyzer.generate_mock_data(days=365)

# Calcular métricas
metrics = analyzer.calculate_metrics()
print(metrics)

# Generar gráficos
analyzer.plot_price_history()
analyzer.plot_volume()
analyzer.plot_price_distribution()
analyzer.plot_market_cap()

# Generar reporte completo
analyzer.generate_report()
```

## Características

1. **Generación de Datos**
   - Datos simulados realistas
   - Precios con tendencia y volatilidad
   - Volumen de trading
   - Capitalización de mercado

2. **Análisis Técnico**
   - Precio actual, máximo y mínimo
   - Volumen promedio
   - Volatilidad
   - Retorno total
   - Capitalización de mercado

3. **Visualizaciones**
   - Historial de precios
   - Volumen de trading
   - Distribución de precios
   - Capitalización de mercado

4. **Reportes**
   - Generación automática de reportes
   - Gráficos guardados como imágenes
   - Métricas en archivo de texto

## Ejemplo de Salida

El programa generará:

1. **Métricas en Consola**:
```
Métricas de Bitcoin:
precio_actual: 30,000.00
precio_maximo: 35,000.00
precio_minimo: 25,000.00
volumen_promedio: 1,000.00
volatilidad: 500.00
retorno_total: 50.00
market_cap_actual: 600,000,000,000.00
```

2. **Gráficos**:
- `reports/price_history.png`: Historial de precios
- `reports/volume.png`: Volumen de trading
- `reports/price_distribution.png`: Distribución de precios
- `reports/market_cap.png`: Capitalización de mercado

3. **Reporte de Métricas**:
- `reports/metrics.txt`: Archivo con todas las métricas calculadas

## Personalización

Puedes personalizar el análisis modificando:

1. **Período de Análisis**:
```python
analyzer.generate_mock_data(days=180)  # 6 meses
```

2. **Criptomoneda**:
```python
analyzer = CryptoAnalyzer(symbol="ETH")  # Ethereum
```

3. **Directorio de Reportes**:
```python
analyzer.generate_report('reports/custom')
```

## Contribuir

Las contribuciones son bienvenidas. Por favor, sigue estos pasos:

1. Haz un Fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE para más detalles.

## Contacto

Tu Nombre - [@tutwitter](https://twitter.com/tutwitter) - email@example.com

Link del Proyecto: [https://github.com/tuusuario/nombre-del-proyecto](https://github.com/tuusuario/nombre-del-proyecto) 