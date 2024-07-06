"""
Desarrolle un programa completo en Python que permita generar una sucesión de 13000 números enteros aleatorios negativos
usando como semilla del generador al valor 1779 (es decir, random.seed(1779)). Los valores de cada uno de esos 13000
números deben estar entre -25000 y -1000 (incluidos ambos - DEBE usar random.randint(-25000, -1000) para generar cada
uno de estos números).

A modo de elemento de control, y para que cada estudiante sepa si la secuencia que está generando es la correcta,
indicamos aquí cuánto debe valor la suma de todos los números generados con el mecanismo indicado:
    - Suma de todos ls números generados: -167972204
A partir de esta sucesión, el programa debe:
    1) Determinar la suma de todos los números que eran pares; la suma de todos los que eran divisibles por 5; y la
    cantidad de números que eran mayores o iguales que -2000 pero además no eran divisibles por 4.
    2) Determinar el promedio entero de todos los números generados que eran mayores que -6000 pero menores que -2000 y
    que además no sean divisibles por 6. Aclaración: NO se pide el promedio redondeado, sino el promedio truncado, sin
    decimales.
    3) Determinar el menor entre todos los números generados que estén comprendidos entre -20000 y -5000 (incluidos
    ambos) y que sean también divisibles por 8.
    4) Determinar el porcentaje entero que la cantidad de números mayores que -3000 pero que sean divisibles por 3
    representa sobre la cantidad total de números procesados. Aclaración: NO se pide el porcentaje redondeado, sino el
    truncado, sin decimales. Observación: en el cálculo de este porcentaje, haga primero la multiplicación que
    corresponda, y luego la división.
"""
import random

random.seed(1779)

# Para comprobación de los números generados
suma = 0

# Consigna 1
suma_pares = suma_div_5 = cont_may_2000_no_div_4 = 0
# Consigna 2
suma_6000_2000_no_div_6 = cont_6000_2000_no_div_6 = 0
# Consigna 3
menor = 0
# Consigna 4
cont_may_3000_div_3 = 0

for _ in range(13000):
    numero = random.randint(-25000, -1000)
    suma += numero

    # Consigna 1
    # Sumo todos los números pares
    if numero % 2 == 0:
        suma_pares += numero
    # Sumo todos los números divisibles por 5
    # Lo habia puesto como en la linea 49 pero no estaba considerando que un número puede ser múltiplo de 5 y 2 (Ej.:10)
    # elif numero % 5 == 0:
    if numero % 5 == 0:
        suma_div_5 += numero
    # Cuento todos los números mayores a 2000 que NO son divisibles por 4
    if numero >= -2000 and numero % 4 != 0:
        cont_may_2000_no_div_4 += 1

    # Consigna 2
    # Sumo y cuento todos los números en el intervalo (-6000,-2000) que NO son divisibles por 6
    if -6000 < numero < -2000 and numero % 6 != 0:
        suma_6000_2000_no_div_6 += numero
        cont_6000_2000_no_div_6 += 1

    # Consigna 3
    # Determino el menor número generado en el intervalo [-20000, -5000] que SI son divisibles por 8
    if -20000 <= numero <= -5000 and numero % 8 == 0:
        if numero < menor:
            menor = numero

    # Consigna 4
    # Cuento los números mayores que -3000 que SI son divisibles por 3
    if numero > -3000 and numero % 3 == 0:
        cont_may_3000_div_3 += 1

assert suma == -167972204
# Calculo el promedio que me piden en el punto 2
promedio_consigna_2 = suma_6000_2000_no_div_6 // cont_6000_2000_no_div_6
# Calculo el porcentaje que me piden en la consigna 4
porcentaje_consigna_4 = cont_may_3000_div_3 * 100 // 13000

print("Consigna 1")
print(f"La suma de todos los números pares es {suma_pares}")
print(f"La suma de todos los números divisibles por 5 es {suma_div_5}")
print(f"La cantidad de números >= -2000 que no son divisibles por 4 es {cont_may_2000_no_div_4}")
print("Consigna 2")
print(f"El promedio entero de todos los números en el intervalo (-6000, -2000) que no son divisibles por 6 es "
      f"{promedio_consigna_2}")
print("Consigna 3")
print(f"El menor número dentro del intervalo [-20000, -5000] que es divisible por 8 es {menor}")
print("Consigna 4")
print(f"El porcentaje entero de los números mayores que -3000 que son divisibles por 3 sobre el total es "
      f"{porcentaje_consigna_4}%")
