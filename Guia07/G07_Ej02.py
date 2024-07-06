"""
Cargar por teclado dos números, e imprimir los números que se encuentran comprendidos entre ellos, en forma ascendente
y descendente
"""

numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número distinto: "))

# Primero ordenamos los números
if numero1 > numero2:
    numero1, numero2 = numero2, numero1

# Ahora los convertimos en los impares mas cercanos
if numero1 % 2 == 0:
    numero1 += 1
if numero2 % 2 == 0:
    numero2 -= 1

# Imprimimos de forma ascendente
print("Números de forma ascendente:")
for i in range(numero1, numero2, 2):
    print(i, end=" ")
print()

# Imprimimos de forma descendente
print("Números de forma descendente:")
for i in range(numero2, numero1, -2):
    print(i, end=" ")
