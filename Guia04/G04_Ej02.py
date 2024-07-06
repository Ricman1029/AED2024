"""
Se necesita desarrollar un programa que permita calcular la suma de tres números. Si el resultado es mayor a 10 dividir
por 2 (mostrar su resultado sin decimales), en caso contrario elevar el resultado al cubo.
"""

numero1 = int(input("Ingrese un primer número: "))
numero2 = int(input("Ingrese un segundo número: "))
numero3 = int(input("Ingrese un tercer número: "))

suma = numero1 + numero2 + numero3

if suma > 10:
    resultado = suma / 2
else:
    resultado = suma ** 3

print(resultado)
