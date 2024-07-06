"""
Se solicita realizar un programa que permita ingresar tres temperaturas correspondientes a diferentes momentos de un
día y determinar:
    - Cuál es el promedio de las temperaturas.
    - Si existe alguna temperatura que sea mayor al promedio.
"""

temperatura1 = int(input("Ingrese la primer temperatura: "))
temperatura2 = int(input("Ingrese la segunda temperatura: "))
temperatura3 = int(input("Ingrese la tercer temperatura: "))

promedio = (temperatura1 + temperatura2 + temperatura3) / 3

max_temperatura = max(temperatura1, temperatura2, temperatura3)

if max_temperatura > promedio:
    temperatura_mayor_que_promedio = "Existe una temperatura mayor al promedio."
else:
    temperatura_mayor_que_promedio = "No existe una temperatura mayor al promedio."

print(f"La temperatura promedio es {promedio}")
print(temperatura_mayor_que_promedio)

