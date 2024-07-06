"""
Desarrolle un programa completo en Python que permita generar una sucesión de 25000 números enteros aleatorios, usando
como semilla del generador el número 20220512 (es decir random.seed(20220512)). Los valores de cada uno de esos 25000
números deben estar entre 1 y 45000 (incluidos ambos) (DEBE usar random.randint(1, 45000) para generar esos números).
A partir de esa sucesión el programa debe:

1) Determinar la cantidad de números múltiplos de 3 y también la cantidad de números múltiplos de 5 pero no de 3 y
finalmente la cantidad de números que no cumplen ninguna de las 2 condiciones.
2) Indicar el mayor entre todos los números comienzan con el dígito 1, es decir 1234 comienza con 1 y 2345 no comienza
con 1.
3) Indicar el promedio entero truncado de los números generados que son pares y múltiplos de 11.
4) Indicar el porcentaje entero que representa cada contador del punto 1. Aclaración 1: NO se pide el porcentaje
redondeado, sino el porcentaje truncado, sin decimales. Aclaración 2: en el cálculo de este porcentaje, haga primero la
multiplicación que corresponda, y luego la división.
Cuando finalice, en las consignas que siguen en este mismo cuestionario, se le pedirá que informe cada uno de estos
resultados, y también se le pedirá que suba el archivo de código fuente con el programa desarrollado (por lo que tenga
muy presente en donde dejó ese archivo). Habrá también UNA pregunta de opciones múltiples referida a este mismo
enunciado o a temas relacionados con él.
"""
import random

random.seed(20220512)

# Consigna 1
cont_mult_3 = cont_mult_5_no_3 = cont_no_mult_5_3 = 0
# Consigna 2
mayor = None
# Consigna 3
cont_par_div_11 = 0
suma_par_div_11 = 0

for _ in range(25000):
    aleatorio = random.randint(1, 45000)

    # Consigna 1
    if aleatorio % 3 == 0:
        cont_mult_3 += 1
    elif aleatorio % 5 == 0:
        cont_mult_5_no_3 += 1
    else:
        cont_no_mult_5_3 += 1

    # Consigna 2
    # Primero obtengo el primer dígito del número aleatorio y me fijo si es igual a 1
    primer_dig_de_aleatorio = int(str(aleatorio)[0])
    if primer_dig_de_aleatorio == 1:
        # Busco el mayor de todos los aleatorios que cumplan la condición anterior
        if mayor is None or aleatorio > mayor:
            mayor = aleatorio

    # Consigna 3
    if aleatorio % 2 == 0 and aleatorio % 11 == 0:
        cont_par_div_11 += 1
        suma_par_div_11 += aleatorio

# Consigna 3
# Calculo el promedio de los pares múltiplos de 11
promedio_par_div_11 = suma_par_div_11 // cont_par_div_11

# Consigna 4
porc_mult_3 = cont_mult_3 * 100 // 25000
porc_mult_5_no_3 = cont_mult_5_no_3 * 100 // 25000
porc_no_mult_5_3 = cont_no_mult_5_3 * 100 // 25000

print("Consigna 1:")
print(f"Multiplos de 3: {cont_mult_3}")
print(f"Multiplos de 5 pero no de 3: {cont_mult_5_no_3}")
print(f"No multiplos de 5 ni 3: {cont_no_mult_5_3}")
print("Consigna 2:")
print(f"El mayor de los números que comienzan con 1: {mayor}")
print(f"Consigna 3:")
print(f"Promedio entero de números pares multiplos de 11: {promedio_par_div_11}")
print("Consigna 4:")
print(f"Porcentaje entero de multiplos de 3: {porc_mult_3}")
print(f"Porcentaje entero de multiplos de 5 pero no de 3: {porc_mult_5_no_3}")
print(f"Porcentaje entero de NO multiplos de 5 o 3: {porc_no_mult_5_3}")
