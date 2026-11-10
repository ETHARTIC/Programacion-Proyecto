# Este docstring describe de forma general el objetivo del módulo.
"""Módulo para calcular el presupuesto disponible y el porcentaje sobre el sueldo nominal."""

# Constante que representa el porcentaje mínimo de dinero disponible que dispara la alerta.
# 0.15 equivale al 15%.
PORCENTAJE_ALERTA = 0.15


# Definimos una función con un nombre descriptivo y en snake_case.
def calcular_presupuesto(sueldo, gastos_fijos):
    """Calcula el monto disponible y la proporción sobre el sueldo nominal."""

    # sum() permite sumar todos los elementos de la lista de gastos directamente.
    # Esto reemplaza el bucle manual que aparecía en la versión original.
    total_gastos = sum(gastos_fijos)

    # Restamos los gastos al sueldo para saber cuánto dinero queda.
    disponible = sueldo - total_gastos

    # Comprobamos si el dinero disponible está por debajo del 15% del sueldo.
    if disponible < sueldo * PORCENTAJE_ALERTA:
        # El mensaje se escribe en dos partes para no superar la longitud de línea.
        # Python las concatena automáticamente dentro de los paréntesis.
        print(
            "Alerta: queda menos del 15 por ciento "
            "del sueldo disponible para el resto del mes"
        )

    # Devolvemos el monto disponible y su proporción respecto al sueldo.
    return disponible, disponible / sueldo


# Definimos el sueldo utilizado para la prueba.
SUELDO_NOMINAL = 52000

# Definimos los gastos del ejemplo.
GASTOS_DEL_MES = [14500, 6240, 4200, 9800, 3100]

# Ejecutamos la función y mostramos el resultado.
print(calcular_presupuesto(SUELDO_NOMINAL, GASTOS_DEL_MES))
