"""
La final de una carrera de ciclistas tiene n competidores (n se ingresa por teclado)
Desarrollar un programa que permita caragar, por cada competidor, nombre y tiempo de carrera. Luego se pide:
a) Determinar y mostrar el nombre del ganador de la carrera.
b) Ingresar por teclado el tiempo record registrado para dicha carrera. Determinar si el tiempo del ganador es menor al
tiempo record, mostrar un mensaje.
c) Calcular y mostrar el tiempo promedio entre todos los ciclistas.
"""

# Indices de los datos del competidor
nombre = 0
tiempo = 1

# Cantidad de competidores
n = int(input("Ingrese la cantidad de competidores: "))
record = int(input("Ingrese el record de carrera en segundos: "))
suma_tiempos = 0

for competidor in range(n):
    datos_competidor = input(f"Nombre competidor {competidor + 1}: "), \
        int(input(f"Tiempo competidor {competidor + 1} en segundos: "))

    # Buscamos al ganador de la competencia
    if competidor == 0 or ganador[tiempo] > datos_competidor[tiempo]:
        ganador = datos_competidor

    # Sumamos todos los tiempos para después calcular el promedio
    suma_tiempos += datos_competidor[tiempo]

# Mostramos al ganador de la carrera
print(f"El ganador es {ganador[nombre]}")

# Si el ganador batió el record, mostramos un mensaje
if ganador[tiempo] < record:
    print("El record fue superado")

# Calculamos y mostramos el promedio de los tiempos de todos los corredores
promedio = suma_tiempos / n
print(f"El tiempo promedio de la carrera fue {promedio}")
