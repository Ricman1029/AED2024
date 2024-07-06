"""
Desarrollar un programa que, ingresando los dos catetos de un triángulo rectángulo, informe:
    - Valor de la hipotenusa (redondeado a 2 decimales)
    - Valor del lado mayor
    - Valor del lado menor
"""

# Carga de datos
cateto1 = int(input("Ingrese el largo del cateto 1: "))
cateto2 = int(input("Ingrese el largo del cateto 2: "))

# Calculos
hipotenusa = round((cateto1 ** 2 + cateto2 ** 2) ** 0.5, 2)
lado_mayor = max(cateto1, cateto2)
lade_menor = min(cateto1, cateto2)

# Muestra de datos
print(f"Hipotenusa: {hipotenusa}")
print(f"Lado Mayor: {lado_mayor}")
print(f"Lado Menor: {lade_menor}")
