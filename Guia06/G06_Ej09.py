"""
Ingresar de a uno, una serie de números. Encontrar e imprimir el mayor de todos los números pares cuyo número de orden
sea par, el proceso terminará cuando el número leído sea igual a cero.
"""

# Inicializamos las variables que vamos a utilizar
# contador indica la posición del número ingresado en la serie
contador = mayor = 0

# Pedimos al usuario que ingrese el primer número
numero = int(input("Ingrese un número: "))

# Si ingresa el número 0(cero), el bucle finaliza
while numero != 0:
    # Si número ingresado es par, su posición es par y en mayor que "mayor", actualizamos "mayor"
    if contador % 2 == 0 and numero % 2 == 0 and mayor < numero:
        mayor = numero

    # Pedimos al usuario que ingrese un nuevo número y actualizamos contador
    numero = int(input("Ingrese otro número: "))
    contador += 1

# Mostramos el resultado
print(f"El mayor número de todos los números pares cuyo número de orden fue par es {mayor}.")
