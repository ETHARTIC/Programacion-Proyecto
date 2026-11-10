# Proyecto final B: portafolio de cine

Análisis para Arroyo Capital de una cartera hipotética de USD 500 millones. El cuaderno audita los datos de películas e IPC, calcula valores reales y ROI, compara riesgo y retorno por segmento, y simula una propuesta de inversión. Los ocho gráficos interactivos también están disponibles como archivos HTML en `salidas/`.

## Requisitos

Python 3.11 o superior. Desde la raíz del repositorio:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Reproducir

1. Conservar `datos/peliculas.csv` y `datos/ipc_eeuu.csv` sin cambios.
2. Abrir `notebooks/Proyecto_Final_B_Portafolio_Cine.ipynb` en Jupyter o VS Code con el entorno creado.
3. Ejecutar todas las celdas de arriba hacia abajo, desde la raíz del repositorio o desde `notebooks/`.
4. Revisar las tablas y gráficos dentro del cuaderno. Los HTML se regeneran en `salidas/`.

## Estructura

- `datos/`: datos originales del curso.
- `instrucciones/`: consigna original.
- `clases/`: material usado para seguir las prácticas del curso.
- `notebooks/`: cuaderno principal y copia solicitada del trabajo inicial.
- `salidas/`: gráficos interactivos HTML.

Los resultados son descriptivos. La recaudación en salas no equivale a ganancia contractual del fondo; la simulación explicita sus supuestos de costos y reparto.
