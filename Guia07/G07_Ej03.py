"""
Ingresar por teclado los sueldos de un vededor, correspondientes al primer semestre del año y luego:
a) Calcular su aguinaldo, sabiendo que es la mitad del sueldo más alto del período.
b) Determinar en qué mes reibió el sueldo más bajo del período
c) Informar el sueldo promedio del semestre
"""

suma = 0

for i in range(1, 7):
    sueldo = int(input(f"Ingrese el sueldo del mes {i}: "))

    # Inicializamos las variables mayor y menor
    if i == 1:
        mayor = sueldo
        menor = sueldo
        mes_menor_sueldo = i

    # Determinamos el sueldo mas alto
    if mayor < sueldo:
        mayor = sueldo

    # Determinamos el sueldo mas bajo
    if menor > sueldo:
        menor = sueldo
        mes_menor_sueldo = i

    # Sumamos los sueldos del semestre para obtener el promedio
    suma += sueldo

promedio = suma / 6

print(f"Le corresponde un aguinaldo de {mayor / 2}")
print(f"El mes con el sueldo mas bajo fue el mes {mes_menor_sueldo}")
print(f"El promedio del semestre es {promedio}")
