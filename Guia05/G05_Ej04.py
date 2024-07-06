"""
Un observatorio meteorológico ha tomado el registro de temperaturas en distintos momentos del día. Se solicita el
desarrollo de un programa que facilite información estadísticas de ellas.
El usuario debe ingresar cuatro valores de temperatura (considerar que son valores enteros).
Los requerimientos funcionales son:
    a) Promedio de temperatura diaria.
    b) Temperatura máxima.
    c) Temperatura mínima.
    d) Informar con un mensaje si algunas de las temperaturas supera a la temperatura promedio.
"""

# Carga de datos
temperatura1 = int(input("Ingrese la primer temperatura: "))
temperatura2 = int(input("Ingrese la segunda temperatura: "))
temperatura3 = int(input("Ingrese la tercer temperatura: "))
temperatura4 = int(input("Ingrese la cuarta temperatura: "))

# Procesos
promedio = (temperatura1 + temperatura2 + temperatura3 + temperatura4) / 4

# Temperatura máxima
if temperatura1 < temperatura2:
    temperatura1, temperatura2 = temperatura2, temperatura1
if temperatura1 < temperatura3:
    temperatura1, temperatura3 = temperatura3, temperatura1
if temperatura1 < temperatura4:
    temperatura1, temperatura4 = temperatura4, temperatura1

# Temperatura mínima
if temperatura4 > temperatura2:
    temperatura4, temperatura2 = temperatura2, temperatura4
if temperatura4 > temperatura3:
    temperatura4, temperatura3 = temperatura3, temperatura4


# Mostrar resultados
print(f"La temperatura promedio es {promedio}")
print(f"La temperatura maxima es {temperatura1}")
print(f"La temperatura minima es {temperatura4}")

if temperatura1 > promedio:
    print(f"La temperatura {temperatura1} es mayor al promedio.")
if temperatura2 > promedio:
    print(f"la temperatura {temperatura2} es mayor al promedio.")
if temperatura3 > promedio:
    print(f"la temperatura {temperatura3} es mayor al promedio.")
if temperatura4 > promedio:
    print(f"la temperatura {temperatura4} es mayor al promedio.")
