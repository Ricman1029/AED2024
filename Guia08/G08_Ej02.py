"""
Ingresar una secuencia de números, de a uno por vez, la carga finaliza cuando el usuario ingresa el cero. Determinar

a) Porcentaje que representan los números divisibles por 3 sobre el total de números ingresados en la secuencia

b) Determinar la cantidad de números que son el cuadrado del número anterior

c) Determinar la posición del mayor elemento impar de la secuencia
"""

# Inicialización de variables
cont_total = cont_div_3 = cont_cuad_ant = numero_anterior = posicion_mayor = 0
mayor = None

# Se ingrsa el primer número
numero = int(input("Ingrese un número (con cero termina): "))
cont_total += 1

while numero != 0:
    # Contamos los numeros divisibles por 3
    if numero % 3 == 0:
        cont_div_3 += 1

    # Contamos los números que son el cuadrado del número anterior
    if numero == numero_anterior ** 2:
        cont_cuad_ant += 1

    # Nos fijamos si el número es impar
    if numero % 2 != 0:
        # Buscamos el mayor y guardamos su posicion
        if mayor == None or numero > mayor:
            mayor = numero
            posicion_mayor = cont_total

    numero_anterior = numero
    numero = int(input("Ingrese un número (con cero termina): "))
    cont_total += 1

porcentaje = cont_div_3 * 100 / cont_total

print(f"El porcentaje de numeros divisibles por 3 es {porcentaje}%")
print(f"La cantidad de números que son el cuadrado del anterior es {cont_cuad_ant}")
print(f"La posicion del mayor número impar es {posicion_mayor}")