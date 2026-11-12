# Arroyo Capital: inversión y portafolio en cine

Proyecto final B de Programación Analítica II.

**Integrantes:** Nicolás Gómez y Ethan Schcolnik.

Analizamos una base histórica de películas y el IPC de Estados Unidos para proponer cómo distribuir USD 500 millones en cine durante tres años. Primero revisamos y limpiamos los datos, después comparamos el retorno y el riesgo de distintos grupos y simulamos los resultados de la propuesta.

## Archivos y carpetas

- [`notebooks/Proyecto_Final_B_Portafolio_Cine.ipynb`](notebooks/Proyecto_Final_B_Portafolio_Cine.ipynb): notebook principal con las cinco etapas, el código y las observaciones.
- `datos/`: archivos originales `peliculas.csv` e `ipc_eeuu.csv`. La limpieza se hace en el notebook.
- `salidas/`: gráficos PNG y HTML, tablas de la propuesta y resultados de la simulación.
- `instrucciones/`: consigna y descripción de los datos.
- [`requirements.txt`](requirements.txt): librerías necesarias para ejecutar el proyecto.
- [`.gitignore`](.gitignore): excluye entornos virtuales, archivos temporales de Python y Jupyter y archivos locales del sistema. También incluye la regla `/datos/*.csv`; los CSV del caso ya están versionados y permanecen en el repositorio.

## Preparar el entorno

Se necesita Python 3.11 o superior. Desde la raíz del repositorio, crear y activar un entorno virtual e instalar las dependencias.

En Windows, con PowerShell:

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

Con el entorno activado, registrarlo como kernel de Jupyter:

```bash
python -m ipykernel install --user --name portafolio-cine --display-name "Python (Portafolio de cine)"
```

## Ejecutar el proyecto

1. Desde la raíz del repositorio y con el entorno activado, abrir Jupyter con `python -m notebook`.
2. Abrir `notebooks/Proyecto_Final_B_Portafolio_Cine.ipynb` y seleccionar el kernel `Python (Portafolio de cine)`.
3. Reiniciar el kernel y ejecutar todas las celdas de arriba abajo, en el orden del notebook.
4. Revisar los resultados y las observaciones debajo del código. Los gráficos se guardan en `salidas/` y las tablas se muestran en las celdas.

También se puede abrir el notebook con VS Code y seleccionar el mismo kernel. Las rutas funcionan desde la raíz del proyecto o desde `notebooks/`. Los gráficos HTML interactivos necesitan conexión a internet para cargar Plotly.

## Qué incluye el análisis

El notebook revisa duplicados, faltantes y valores sospechosos; ajusta los importes por inflación; y compara el retorno y el riesgo por género y franquicia. La sección 4.2 muestra cómo cambian la media y la mediana cuando apartamos temporalmente los resultados extremos.

La propuesta distribuye los USD 500 millones entre cuatro grupos y 19 proyectos. Comparamos el dinero disponible para producir cada película con el presupuesto mediano de su grupo y proponemos un reparto durante los tres años del caso.

La simulación usa 10.000 sorteos por supuesto. Compara proyectos independientes con resultados compartidos dentro de cada grupo y muestra el ROI, el capital final y la probabilidad de pérdida con histogramas, boxplots y gráficos de barras. También probamos qué pasa al limitar los éxitos extremos y aumentar el costo de marketing.

## Supuestos de la propuesta

Los USD 500 millones incluyen producción y marketing. En el escenario base, marketing y distribución equivalen al 50% del presupuesto de producción y el estudio recibe el 50% de la boletería.

Los montos se expresan en dólares de 2020 para compararlos con la base histórica. Para invertir en otro año habría que actualizar el capital y los costos. La regla de 2,5x se informa por separado del ROI estimado, cuyo equilibrio queda en 3x con estos supuestos.

Los retornos se estiman con medianas y simulaciones. El riesgo depende de los supuestos de costos y de cómo se relacionan los resultados de las películas. Si marketing sube al 100% de producción, mantener los mismos proyectos requiere USD 666,7 millones y supera el capital disponible.

El ROI de salas es una estimación del proyecto, no una tasa anual ni el retorno contractual del fondo. Las limitaciones y los grupos que no priorizaríamos se explican en la sección 5.5. La presentación ejecutiva de diez minutos es un entregable separado.
