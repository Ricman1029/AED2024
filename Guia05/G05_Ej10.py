"""
Desarrollar un programa que permita al usuario jugar contra la computadora el clásico "Piedra, Papel o Tijera" y
determina cuál de ellos es el ganador.
Las reglas son:
    - La piedra aplasta (o rompe) la tijera. (Gana la piedra)
    - La tijera corta el papel. (Gana la tijera)
    - El papel envuelve la piedra. (Gana el papel)
    - Si los dos jugadores eligen el mismo elemento, empatan.
"""
import random

# El usuario elige una opción
jugador = input("Piedra, papel o tijera?: ")

# El ordenador genera una de las tres opciones válidas, y la imprime
compu = random.choice(("piedra", "papel", "tijera"))
print(f"La compu eligió {compu}.")

# Se determina el ganador, o si hubo empate se avisa.
if jugador == "piedra" and compu == "tijera" \
        or jugador == "papel" and compu == "piedra" \
        or jugador == "tijera" and compu == "papel":
    print("Ganaste!")
elif jugador == compu:
    print("Empate.")
else:
    print("Perdiste.")
