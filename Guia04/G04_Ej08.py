"""
Simular un juego en el que se lanzan dos dados.
Si ambos dados son iguales o la suma entre ellos es impar, gana el usuario. En caso contrario, gana la máquina.
"""

import random

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

if dado1 == dado2 or (dado1 + dado2) % 2 == 1:
    resultado = "Ganaste!"
else:
    resultado = "Perdiste :/"

print(f"Dado 1: {dado1}")
print(f"Dado 2: {dado2}")
print(resultado)
