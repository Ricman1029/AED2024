"""
Turno 01:
Desarrolle un programa completo en Python que permita generar una sucesión de  17000 números
enteros aleatorios, usando como semilla del generador al valor 1157 (es decir, random.seed(1157)). Los valores de
cada uno de esos 17000 números deben estar entre 1000 y 37000 (incluidos ambos
DEBE usar random.randint(1000, 37000) para generar cada uno de estos números).
A modo de elemento de control, y para que cada estudiante sepa si la secuencia que está generando es la correcta,
indicamos aquí cuánto debe valer la suma de todos los números generados con el mecanismo indicado:
✓ Suma de todos los números generados: 322152298
A partir de esa sucesión, el programa debe:
    1. Determinar cuántos de esos números eran mayores o iguales a 1000 pero menores que 15000, cuál es la
        suma de los que eran mayores o iguales que 15000 y menores que 30000, y cuántos eran mayores o
        iguales que 30000.
    2. Determinar el promedio entero de los números generados que eran divisibles por 7 pero no por 3.
        Aclaración: NO se pide el promedio redondeado, sino truncado, sin decimales.
    3. Determinar el menor entre todos los números generados que sean impares.
    4. Determinar el porcentaje entero que representa la cantidad de números pares generados sobre la cantidad
        total de números procesados. Aclaración: NO se pide el porcentaje redondeado, sino truncado, sin
        decimales. Observación: en el cálculo de este porcentaje, haga primero la multiplicación que corresponda, y
        luego la división.
"""
import random

random.seed(1157)

contador_bucle = suma = 0
# Consigna 1
contador_intervalo = contador_mayores = suma_intervalo = 0
acumulador_div_7_no_3 = contador_div_7_no_3 = 0

contador_par = 0
no_hay_menor = True

while contador_bucle < 17000:
    # Genero número aleatorio y actualizo el contador
    numero = random.randint(1000, 37000)
    contador_bucle += 1

    # Cuento todos los números entre 1000 y 15000
    if 1000 <= numero < 15000:
        contador_intervalo += 1
    # Sumo todos los números entre 15000 y 30000
    elif 15000 <= numero < 30000:
        suma_intervalo += numero
    # Cuento todos los números mayores a 30000
    else:
        contador_mayores += 1

    # Sumo todos los números divisibles por 7 pero no por 3 (para calcular promedio después)
    if numero % 7 == 0 and numero % 3 != 0:
        acumulador_div_7_no_3 += numero
        contador_div_7_no_3 += 1

    # Me fijo si el número generado es impar
    if numero % 2 != 0:
        # Si es el primer impar generado, se lo asigno a menor
        if no_hay_menor:
            menor = numero
            no_hay_menor = False
        # Si ya hay un menor asignado, determino el menor número impar generado
        elif numero < menor:
            menor = numero
    # Si el número es par, actualizo el contador de número pares
    else:
        contador_par += 1

    # Es para chequear los números generados
    suma += numero

# Calculo el promedio entero de todos los números divisibles por 7 pero no por 3
promedio = acumulador_div_7_no_3 // contador_div_7_no_3

# Determino el porcentaje entero de todos los números pares sobre el total de números generados
porcentaje = contador_par * 100 // contador_bucle

print(f"Suma: {suma}")
print(f"Hay {contador_intervalo} números en el intervalo [1000, 15000)")
print(f"La suma de los números en el intervalo [15000, 30000) es de {suma_intervalo}")
print(f"Hay {contador_mayores} números mayores a 30000")
print(f"El promedio entero de los números generados que eran divisibles por 7 pero no por 3 es {promedio}")
print(f"El menor número impar generado es {menor}")
print(f"El porcentaje entero de números pares generados sobre el total de números generados es {porcentaje}%")
