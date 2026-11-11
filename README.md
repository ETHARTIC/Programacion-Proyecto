# Arroyo Capital: inversion en cine

Proyecto final B de Programacion Analitica II — Ethan Schcolnik y Nicolas Gomez.

Analizamos la base historica de peliculas y el IPC de Estados Unidos para proponer una distribucion de USD 500 millones. El notebook revisa la calidad de los datos, ajusta los importes por inflacion, compara retorno y riesgo y simula una cartera.

## Preparar el entorno

Se necesita Python 3.11 o superior. Desde la raiz del repositorio:

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

1. Abrir Jupyter con `python -m notebook` desde la raiz del repositorio.
2. Abrir `notebooks/Proyecto_Final_B_Portafolio_Cine.ipynb`.
3. Seleccionar el entorno instalado y ejecutar todas las celdas de arriba abajo.
4. Revisar las observaciones que aparecen despues del codigo. Los graficos se guardan en `salidas/`; las tablas quedan mostradas en las celdas.

Tambien se puede abrir el notebook con VS Code usando el mismo entorno. Las rutas funcionan desde la raiz o desde `notebooks/`. Los graficos HTML interactivos necesitan conexion para cargar Plotly.

## Que contiene cada carpeta

- `datos/`: CSV originales, que se conservan sin modificaciones.
- `notebooks/Proyecto_Final_B_Portafolio_Cine.ipynb`: version principal para la entrega y la presentacion.
- `salidas/`: graficos PNG y HTML generados por el notebook principal.
- `instrucciones/`: consigna y descripcion de los datos.
- `clases/`: material de referencia del curso y ejercicios.

## Supuestos de la propuesta

Los USD 500 millones cubren produccion y marketing. En el escenario base, marketing y distribucion equivalen al 50 % del presupuesto de produccion y el estudio recibe la mitad de la boleteria. La propuesta tiene cuatro grupos y 19 proyectos, y compara el presupuesto de produccion disponible por pelicula con su mediana historica.

Los montos se expresan en dolares de 2020 para compararlos con la base: al invertir en otro ano se debe actualizar el capital y los costos. La regla comercial de 2,5× se informa por separado del ROI estimado, cuyo equilibrio queda en 3× bajo estos supuestos.

La simulacion compara proyectos independientes con resultados compartidos por grupo y prueba sensibilidad a exitos extremos y mayor marketing. Son escenarios historicos condicionados a los supuestos, no garantias ni retornos contractuales del fondo. La presentacion ejecutiva de diez minutos es un entregable separado.
