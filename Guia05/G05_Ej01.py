"""
Realizar un programa que tome tres números, los ordene de mayor a menor. Sobre los valores ordenados diga si el tercero
es el resto de la división de los dos primeros.
"""

# numero1 representa al mayor, numero2 al medio, numero3 al menor
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

if not (numero1 >= numero2 >= numero3):
    if numero1 < numero2:
        numero1, numero2 = numero2, numero1
    if numero1 < numero3:
        numero1, numero3 = numero3, numero1
    if numero2 < numero3:
        numero2, numero3 = numero3, numero2

if numero3 == numero1 % numero2:
    respuesta = "sí"
else:
    respuesta = "no"

print(f"Mayor: {numero1} - Medio: {numero2} - Menor: {numero3}\n"
      f"El menor número {respuesta} es el resto de la division del mayor y el menor.")
