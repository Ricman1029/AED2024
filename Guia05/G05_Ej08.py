"""
Desarrollar un programa para simular el juego de dados que se describe a continuación:

INICIO DEL JUEGO
Participan 2 jugadores. Para comenzar, se debe ingresar el puntaje récord del juego. Los jugadores deberán acumular
puntos en dos rondas para ganar y (eventualmente) superar el récord.

PIMERA RONDA
Se lanzan 2 dados. El puntaje en juego es el total de los daods. Si la suma de ambos dados es impar, el jugador 1 se
queda con el puntaje y el jugador 2 con 0 puntos. Si la suma es par, el puntaje se asigna al jugador 2 mientras que el
jugador 1 queda con 0.

SEGUNDA RONDA
Se lanzan nuevamente los 2 dados. Si la suma de ambos es impar, al jugador 1 se le agregan tantos puntos como indique el
dado de mayor valor, mientras que al jugador 2 se le quitan tantos puntos como indique el dado de menor valor. Si la
suma es par, sucede lo contrario: el jugador 2 suma a su puntaje el dado de mayor valor y el jugador 1 resta el de
menor valor.

DETERMINACIÓN DEL GANADOR
El jugador que haya obtenido mayor puntaje será el ganador (considerar que pueden empatar). Informar además si el récord
fue superado por alguno de ellos (o ambos)
"""
import random

# Comienzo del juego
record = int(input("Ingrese el puntaje récord: "))

# Ronda 1
# Se lanzan dos dados y se suman sus valores
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
suma = dado1 + dado2

# Si la suma de los dados es par, los puntos van al jugador 2
if suma % 2 == 0:
    jugador1 = 0
    jugador2 = suma
# Sino, van al jugador 1
else:
    jugador1 = suma
    jugador2 = 0

# Ronda 2
# Se lanzan nuevamente los dados
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
suma = dado1 + dado2

# Si la suma de los dados es par,
# se le suma el dado mas alto al jugador 2
# y se le resta el dado mas bajo al jugadr 1
if suma % 2 == 0:
    jugador1 -= min(dado1, dado2)
    jugador2 += max(dado1, dado2)
# Sino, pasa lo contrario
else:
    jugador1 += max(dado1, dado2)
    jugador2 -= min(dado1, dado2)

# Determinamos al ganador en base a los puntos conseguidos
if jugador1 == jugador2:
    print("Empate.")
elif jugador1 > jugador2:
    print("Gana el jugador 1!")
else:
    print("Gana el jugador 2!")

# Informamos si el récord fue batido
if jugador1 > record:
    print(f"El jugador 1 obtuvo {jugador1} puntos, superando el récord de {record} puntos.")
if jugador2 > record:
    print(f"El jugador 2 obtuvo {jugador2} puntos, superando el récord de {record} puntos.")
