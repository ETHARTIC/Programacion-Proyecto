# Arroyo Capital: inversión en cine

Proyecto final B de Programación Analítica II — Ethan Schcolnik y Nicolás Gómez.

Analizamos la base histórica de películas y el IPC de Estados Unidos para proponer una distribución de USD 500 millones. El notebook revisa la calidad de los datos, ajusta los importes por inflación, compara retorno y riesgo y simula una cartera.

## Preparar el entorno

Se necesita Python 3.11 o superior. Desde la raíz del repositorio:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

En macOS o Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Ejecutar el proyecto

1. Abrir Jupyter con `python -m notebook` desde la raíz del repositorio.
2. Abrir `notebooks/Proyecto_Final_B_Portafolio_Cine.ipynb`.
3. Seleccionar el entorno instalado y ejecutar todas las celdas de arriba abajo.
4. Revisar las observaciones que aparecen después del código. Los gráficos se guardan en `salidas/`; las tablas quedan mostradas en las celdas.

También se puede abrir el notebook con VS Code usando el mismo entorno. Las rutas funcionan desde la raíz o desde `notebooks/`. Los gráficos HTML interactivos necesitan conexión para cargar Plotly.

## Qué contiene cada carpeta

- `datos/`: CSV originales, que se conservan sin modificaciones.
- `notebooks/Proyecto_Final_B_Portafolio_Cine.ipynb`: versión principal para la entrega y la presentación.
- `notebooks/borradores/`: antecedentes de la limpieza y exploraciones previas. Sus cifras y propuestas no son la versión final; algunos conservan rutas originales de Colab.
- `salidas/`: gráficos PNG y HTML generados por el notebook principal.
- `instrucciones/`: consigna y descripción de los datos.
- `clases/`: material de referencia del curso y ejercicios.

## Supuestos de la propuesta

Los USD 500 millones cubren producción y marketing. En el escenario base, marketing y distribución equivalen al 50 % del presupuesto de producción y el estudio recibe la mitad de la boletería. La propuesta tiene cuatro grupos y 19 proyectos, y compara el presupuesto de producción disponible por película con su mediana histórica.

Los montos se expresan en dólares de 2020 para compararlos con la base: al invertir en otro año se debe actualizar el capital y los costos. La regla comercial de 2,5× se informa por separado del ROI estimado, cuyo equilibrio queda en 3× bajo estos supuestos.

La simulación compara proyectos independientes con resultados compartidos por grupo y prueba sensibilidad a éxitos extremos y mayor marketing. Son escenarios históricos condicionados a los supuestos, no garantías ni retornos contractuales del fondo. La presentación ejecutiva de diez minutos es un entregable separado.

## Herramientas del curso utilizadas

- Clases 1–3: constantes, listas, diccionarios, ciclos, condiciones y funciones.
- Clases 4–5: filtros, limpieza, agrupaciones y cruces de tablas con pandas.
- Clases 6–7: gráficos de Matplotlib, Seaborn y Plotly.
- Clase 10: revisión de calidad, percentiles y sorteos con NumPy.
- Clase 12: tramos de presupuesto con `pd.cut`.

La simulación aplica esas herramientas al caso: cada ciclo representa un escenario y suma los resultados de sus proyectos.
