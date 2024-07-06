"""
Desarrollar un programa que genere al azar tres cartas simulando una mano de truco. A continuación deberá:
    1) Informar si entre las cartas se encuentra el as de espadas
    2) Verificar si las tres cartas son del mismo palo. Si es así, identificar cuál fue la mayor carta.
    En caso contrario, informarlo.
"""
import random


numeros_posibles = 1, 2, 3, 4, 5, 6, 7, 10, 11, 12
palos = "Espada", "Basto", "Copa", "Oro"

# No sé cómo hacer para que generar un número al azar entre 1 y 12 sin contar 8 y 9 y sin usar un loop...
# Puede ser con random.choice()... Terminé de escribirlo y me dí cuenta
carta1 = (random.choice(numeros_posibles), random.choice(palos))
# Ahora no sé cómo hacer para que no me repita la carta sin usar un bucle...
nuevos_numeros = random.randint(1,carta1)



