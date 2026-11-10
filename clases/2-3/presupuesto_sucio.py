# Importamos os y math en el código original, aunque en realidad no se utilizan.
# Esto es justamente una de las cosas que una herramienta como Flake8 puede detectar.
import os
import math


# Nombre de función con mayúsculas iniciales y parámetros sin espacios correctos.
# El objetivo del ejercicio será identificar problemas de estilo y luego corregirlos.
def CalcularPresupuesto(sueldo, gastos_fijos):
    # Iniciamos el acumulador del total de gastos en cero.
    total = 0

    # Recorremos todos los gastos fijos de la lista.
    for g in gastos_fijos:
        # Sumamos cada gasto al acumulador.
        total = total + g

    # El dinero disponible es el sueldo menos el total de gastos.
    disponible = sueldo - total

    # Calculamos cuál sería el 15% del sueldo.
    aux = sueldo * 0.15

    # Si el dinero disponible es menor que ese 15%, mostramos una alerta.
    if disponible < sueldo * 0.15:
        print(
            "Alerta: queda menos del 15 por ciento del sueldo disponible para el resto del mes"
        )

    # Devolvemos dos valores:
    # 1) cuánto dinero queda disponible;
    # 2) qué proporción representa ese disponible sobre el sueldo.
    return disponible, disponible / sueldo


# Sueldo nominal utilizado como ejemplo.
SUELDO_NOMINAL = 52000

# Lista de gastos fijos del mes.
GASTOS_DEL_MES = [14500, 6240, 4200, 9800, 3100]

# Llamamos a la función y mostramos la tupla devuelta.
print(CalcularPresupuesto(SUELDO_NOMINAL, GASTOS_DEL_MES))
