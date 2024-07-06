# TABLERO TENIS

Hacer un programa que permita contabilizar los puntos de un partido de tenis a medida que el mismo se lleva a cabo.

## Definiciones
    
### Puntos
Cuando un jugador gana un punto incremente su puntaje siguiendo la escala 0, 15, 30, 40 y VENTAJA

### Games
* Los puntos se incrementan durante un game. Si el jugador logra una diferencia de 2 puntos a partir del 3er punto ganado, entonces gana un game. 
Por esta razón en caso de estar empatados 40-40 (DEUCE), para ganar el game, un jugador debe ganar 2 puntos seguidos.
* Cuando un jugador gana un punto después de estar empatados en 40, suma un punto y se dice que tiene VENTAJA. 
* Si un jugador tiene VENTAJA y pierde su punto, entonces pierde la VENTAJA y ambos jugadores quedan otra vez igualados en 40. 

### Sets 
* Lo games se suman para cada jugador dentro de un set. 
* El set termina cuando uno de los jugadores llega a 6 games y tiene diferencia de 2 games con su oponente. 
* En caso de no lograr esa diferencia con 6 games, lo puede hacer ganando 7 games (7-5)
* Si ambos jugadores quedan empatados con 6 games cada uno, entonces el set se define en un tiebreak.
* En el tiebreak el primer jugador que llegue a 7 puntos gana, pero debe tener una distancia de dos puntos con su oponente, en caso de no haberla, se sigue jugando hasta lograrla. El jugador que gane el tiebreak gana el set.
* En el último set no hay tiebreak. Se siguen jugando games hasta que un jugador logre 2 games de diferencia con su oponente
* El primer jugador en ganar 2 sets, gana el partido.
* Este programa solo admite juegos a 3 sets.

