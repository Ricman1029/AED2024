"""
Programar una tirada de moneda (opciones: cara o cruz) aleatoriamente. Permitir que un jugador apueste a cara o cruz y
luego informar si acertó o no con su apuesta.
"""
import random

apuesta = input("Ingrese un valor (cara o cruz): ")

lados = "cara", "cruz"
valor = random.choice(lados)

if apuesta == valor:
    respuesta = "Ganaste!"
else:
    respuesta = "Perdiste :("

print(respuesta)
