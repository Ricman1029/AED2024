"""
Turno 06:
Desarrolle un programa completo en Python que permita generar una sucesión de  13000 números
enteros aleatorios negativos, usando como semilla del generador al valor 1779 (es decir, random.seed(1779)). Los
valores de cada uno de esos 13000 números deben estar entre -25000 y -1000 (incluidos ambos
DEBE usar random.randint(-25000, -1000) para generar cada uno de estos números).
A modo de elemento de control, y para que cada estudiante sepa si la secuencia que está generando es la correcta,
indicamos aquí cuánto debe valer la suma de todos los números generados con el mecanismo indicado:
✓ Suma de todos los números generados: -167972204
A partir de esa sucesión, el programa debe:
1. Determinar la suma de todos los números que eran pares; la suma de todos los que eran divisibles por 5, y
la cantidad de números que eran mayores o iguales que -2000, pero además no eran divisibles por 4.
2. Determinar el promedio entero de todos los números generados que eran mayores que -6000, pero
menores que -2000 y que además no sean divisibles por 6. Aclaración: NO se pide el promedio redondeado,
sino el promedio truncado, sin decimales.
3. Determinar el menor entre todos los números generados que estén comprendidos entre -20000 y -5000
(incluidos ambos) y que sean también divisibles por 8.
4. Determinar el porcentaje entero que la cantidad de números mayores que -3000, pero que sean divisibles
por 3 representa sobre la cantidad total de números procesados. Aclaración: NO se pide el porcentaje
redondeado, sino el truncado, sin decimales. Observación: en el cálculo de este porcentaje, haga primero la
multiplicación que corresponda, y luego la división.
"""
import random

random.seed(1779)

# Para comprobar la generación de números
suma = 0
# Consigna 1
suma_pares = suma_div_5 = cont_may_2000_no_div_4 = 0
# Consigna 2
suma_promedio = cont_promedio = 0
# Consigna 3
menor = None
# Consigna 4
cont_porcentaje = 0

for _ in range(13000):
    aleatorio = random.randint(-25000, -1000)
    suma += aleatorio

    # Consigna 1
    # Sumo todos los pares
    if aleatorio % 2 == 0:
        suma_pares += aleatorio
    # Sumo todos los divisibles por 5
    if aleatorio % 5 == 0:
        suma_div_5 += aleatorio
    # Cuento los mayores o iguales a -2000 que NO son divisibles por 4
    if aleatorio >= -2000 and aleatorio % 4 != 0:
        cont_may_2000_no_div_4 += 1

    # Consigna 2
    # Cuento y sumo todos los números que estén entre -6000 incluído y -2000
    if -6000 <= aleatorio < -2000 and aleatorio % 6 != 0:
        suma_promedio += aleatorio
        cont_promedio += 1

    # Consigna 3
    # Primero me fijo que el número esté entre -20000 y -5000 incluidos ambos y que sea múltiplo de 8
    if -20000 <= aleatorio <= -5000 and aleatorio % 8 == 0:
        # busco el menor de todos los números que cumple la condición
        if menor is None or aleatorio < menor:
            menor = aleatorio

    # Consigna 4
    # Cuento todos los números que son mayores que -3000 y divisibles por 3
    if aleatorio > -3000 and aleatorio % 3 == 0:
        cont_porcentaje += 1

assert suma == -167972204

# Consigna 2
# Calculo el promedio entero de los números entre -6000 incluído y -2000
promedio = suma_promedio // cont_promedio

# Consigna 4
# Calculo el porcentaje entero de números mayores que -3000 que son divisibles por 3
porcentaje = cont_porcentaje * 100 // 13000

print("Consigna 1:")
print(f"Suma de todos los pares: {suma_pares}")
print(f"Suma divisibles por 5: {suma_div_5}")
print(f"Cantidad >= -2000 que no son divisibles por 4: {cont_may_2000_no_div_4}")
print("Consigna 2:")
print(f"Promedio entero entre -6000 y -2000 que no son divisibles por 6: {promedio}")
print("Consigna 3:")
print(f"Menor entre -20000 y -5000 divisible por 8: {menor}")
print("Consigna 4:")
print(f"Porcentaje entero mayores que -3000 divisibles por 3: {porcentaje}%")
