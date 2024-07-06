"""
Se necesita desarrollar un programa para el área de recursos humanos de una empresa que permita informar el jornal de
un determinado operario. Usted deberá cargar por teclado el código de turno que el operario trabajó ese día
(1- representa Diurno y 2- representa Nocturno) y la cantidad de horas trabajadas.
La política de trabajo en la empresa es que los operarios de la misma pueden trabajar en el turno diurno o nocturno.
Si un operario trabaja en el turno nocturno el pago es 40.60 poesos la hora, si lo hace en el turno diurno cobra 35.50
pesos la hora.
"""

turno_trabajado = int(input("Ingrese el código del turno trabajado.\n"
                            "'1' representa Diurno.\n"
                            "'2' representa Nocturno.\n"))
horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))

if turno_trabajado == 1:
    jornal = 35.50 * horas_trabajadas
else:
    jornal = 40.60 * horas_trabajadas

print(f"El jornal es: {jornal}")
