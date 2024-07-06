"""
Realizar un programa que genere 15 números aleatorios enteros en el rango del 1 al 100, que representaría la tarjeta
de bingo de una persona. Una vez generados los números aleatorios solicitar al usuario que ingrese 3 números enteros
y a partir de alli mostrar los siguientes mensajes:
    - Si el usuario no marcó ninguno de los números indicarlo diciendo "El jugador tiene mala suerte, no marcó
    ninguna casilla"
    - Caso contrario mostrar "El jugador marcó algún número de la tarjeta"
"""
import random

aleatorio1 = random.randint(1, 100)
aleatorio2 = random.randint(1, 100)
aleatorio3 = random.randint(1, 100)
aleatorio4 = random.randint(1, 100)
aleatorio5 = random.randint(1, 100)
aleatorio6 = random.randint(1, 100)
aleatorio7 = random.randint(1, 100)
aleatorio8 = random.randint(1, 100)
aleatorio9 = random.randint(1, 100)
aleatorio10 = random.randint(1, 100)
aleatorio11 = random.randint(1, 100)
aleatorio12 = random.randint(1, 100)
aleatorio13 = random.randint(1, 100)
aleatorio14 = random.randint(1, 100)
aleatorio15 = random.randint(1, 100)

tupla_aleatorio = aleatorio1, aleatorio2, aleatorio3, aleatorio4, aleatorio5, aleatorio6, aleatorio7, \
     aleatorio8, aleatorio9, aleatorio10, aleatorio11, aleatorio12, aleatorio13, aleatorio14, aleatorio15

numero1 = int(input("Ingrese un primer número del 1 al 100: "))
numero2 = int(input("Ingrese un segundo número del 1 al 100: "))
numero3 = int(input("Ingrese un tercer número del 1 al 100: "))

if numero1 in tupla_aleatorio or numero2 in tupla_aleatorio or numero3 in tupla_aleatorio:
    respuesta = "El jugador marcó algún número de la tarjeta"
else:
    respuesta = "El jugador tiene mala suerte, no marcó ninguna casilla"

print(respuesta)
