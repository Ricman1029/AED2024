"""
Para un análisis estadístico, se pide ingresar 3 valores y determinar:
    - Si alguno de los valores es múltiplo de 5
    - Cuántos de los valores son impares
    - Si el mayor de ellos supera a la suma de los otros 2

(*) Ejercicio tipo parcial
"""

# Se ingresan los 3 valores
valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))
valor3 = int(input("Ingrese el tercer valor: "))

# Procesos
# Se determina si alguno es múltiplo de 5
if valor1 % 5 == 0 or valor2 % 5 == 0 or valor3 % 5 == 0:
    print("Alguno de los valores es múltiplo de 5.")
else:
    print("Ninguno de los valores es múltiplo de 5.")

# Se determina la cantidad de números impares
cantidad_impares = 0
if valor1 % 2 != 0:
    cantidad_impares += 1
if valor2 % 2 != 0:
    cantidad_impares += 1
if valor3 % 2 != 0:
    cantidad_impares += 1
print(f"La cantidad de números impares es {cantidad_impares}.")

# Ponemos al mayor número de los 3 como el valor1
if valor1 < valor2:
    valor1, valor2 = valor2, valor1
if valor1 < valor3:
    valor1, valor3 = valor3, valor1

# Se determina si el mayor de los 3 números supera la suma de los otros dos
if valor1 > valor2 + valor3:
    print("El mayor número supera la suma de los otros dos.")
else:
    print("El mayor número NO supera la suma de los otros dos.")
