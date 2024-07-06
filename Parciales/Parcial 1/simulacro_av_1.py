"""
Desarrolle un programa completo en python que permita generar una sucesión de 20000 números enteros aleatorios, usando
como semilla del generador el número 49( es decir random.seed(49)). Los valores de cada uno de esos 20000 números deben
estar entre 1 y 45000 (incluidos ambos)(DEBE usar random.randint(1, 45000) para generar esos números).
A modo de elemento de control, y para que cada estudiante sepa si la secuencia que está generando es la correcta,
indicamos aquí cuánto debe valer la suma de todos los números generados con el mecanismo indicado:

Suma de todos los números generados: 451459554
A partir de esa sucesión el programa debe:

1) Indicar cuantos números eran múltiplos de 5, cuántos eran múltiplos de 7 y cuántos eran múltiplos de 9.
2) Indicar el mayor entre todos aquellos números cuyo último dígito sea mayor o igual a 5 pero menor o igual a 8.
3) Indicar cuantos números generados son pares menores a 15000.
4) Indicar el porcentaje entero que representa el punto anterior sobre el total de números procesados. Aclaración 1: NO
se pide el porcentaje redondeado, sino el porcentaje truncado, sin decimales. Aclaración 2: en el cálculo de este
porcentaje, haga primero la multiplicación que corresponda, y luego la división.
Cuando finalice, en las consignas que siguen en este mismo cuestionario, se le pedirá que informe cada uno de estos
resultados, y también se le pedirá que suba el archivo de código fuente con el programa desarrollado (por lo que tenga
muy presente en donde dejó ese archivo). Entienda: Si NO sube su código fuente, los profesores procederán a reprobar
manualmente su parcial. Habrá también UNA pregunta de opciones múltiples referida a este mismo enunciado o a temas
relacionados con él.
"""
import random

random.seed(49)

# Para comprobar la generación de números aleatorios
suma = 0
# Consigna 1
cont_mult_5 = cont_mult_7 = cont_mult_9 = 0
# Consigna 2
mayor = None
# Consigna 3
cont_par_menor_15000 = 0

for _ in range(20000):
    aleatorio = random.randint(1, 45000)
    suma += aleatorio

    # Consigna 1
    # Si aleatorio es múltiplo de 5, 7 o 9, actualizamos el contador correspondiente
    if aleatorio % 5 == 0:
        cont_mult_5 += 1
    if aleatorio % 7 == 0:
        cont_mult_7 += 1
    if aleatorio % 9 == 0:
        cont_mult_9 += 1

    # Consigna 2
    # Primero chequeamos que el último dijito de aleatorio este en el intervalo [5, 8]
    if 5 <= aleatorio % 10 <= 8:
        # Si es el caso, buscamos el mayor
        if mayor is None or aleatorio > mayor:
            mayor = aleatorio
            es_1er_mayor = False

    # Consigna 3
    # Chequeamos que aleatorio sea par y menor a 15000 para actualizar su contador
    if aleatorio % 2 == 0 and aleatorio < 15000:
        cont_par_menor_15000 += 1

assert suma == 451459554

porcentaje_par_menor_1500 = cont_par_menor_15000 * 100 // 20000

print("Consigna 1 - Cantidad de números:")
print(f"Múltiplos de 5: {cont_mult_5}")
print(f"Múltiplos de 7: {cont_mult_7}")
print(f"Múltiplos de 9: {cont_mult_9}")

print("Consigna 2:")
if mayor is None:
    print(f"No se generó ningún número cuyo último dígito pertenezca al intervalo [5, 8]")
else:
    print(f"El mayor número cuyo último dígito pertenece al intervalo [5, 8] es el {mayor}")

print("Consigna 3: ")
print(f"Cantidad de números generados que eran pares y menores a 15000: {cont_par_menor_15000}")
print(f"El porcentaje entero de números pares menores a 15000 respecto al total de números generados es: "
      f"{porcentaje_par_menor_1500}%")
