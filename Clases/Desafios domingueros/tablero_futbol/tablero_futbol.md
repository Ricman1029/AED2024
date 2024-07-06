# TABLERO DE FÚTBOL

## Requerimientos
Se solicita hacer un tablero que permita registrar la puntuación de un partido de fútbol.
El programa debe solicitar los nombre del equipo local y del visitante.
Luego, el programa debe permitir a el usuario ingresar las acciones del partido:
    1 si el equipo local metió un gol
    2 si el equipo visitante metió un gol
    3 para indicar que finalizó el primer tiempo o que terminó el partido
    4 para salir


### Salidas durante el partido
La pantalla se debe limpiar al comienzo del programa.
La pantalla se debe limpiar luego de elegir cualquier opción del menú.
El programa debe mostrar el progreso del partido y a continuación el menú de acciones:

```sh
PRIMER TIEMPO
Equipo Local: {NOMBRE LOCAL} - {GOLES LOCAL}
Equipo Visitante: {NOMBRE VISITANTE} - {GOLES VISITANTE}

1. Gol Local
2. Gol Visitante
3. Terminó el primer tiempo
4. Salir
Ingrese una opción:
```
Al finalizar el primer tiempo el programa debe indicar "SEGUNDO TIEMPO" y en el menú el mensaje "Terminó el partido" en lugar de "Terminó el primer tiempo"

```sh

SEGUNDO TIEMPO <--
Equipo Local: {NOMBRE LOCAL} - {GOLES LOCAL}
Equipo Visitante: {NOMBRE VISITANTE} - {GOLES VISITANTE}

1. Gol Local
2. Gol Visitante
3. Terminó el partido <--
4. Salir
Ingrese una opción:
```

### Salidas durante al finalizar el partido

La pantalla se debe limpiar al finalizar el partido para mostrar los resultados.

#### Siempre que haya terminado el partido:
```sh
Cantidad de goles TOTALES: 
Cantidad de goles PRIMER TIEMPO: 
Cantidad de goles SEGUNDO TIEMPO: 
```
#### En caso de empate:
```sh
{NOMBRE LOCAL} y {NOMBRE VISITANTE} empataron con {CANTIDAD GOLES} goles cada uno
```
#### En caso de que haya un ganador y un perdedor:
```sh
{NOMBRE GANADOR} le ganó a {NOMBRE PERDEDOR} por {GOLES GANADOR} a {GOLES PERDEDOR}
```    
#### Si el partido no termina:
```sh
Salió sin finalizar el partido.
```

## Ejemplos de ejecución

Al ejecutarse el programa se debe ver de la siguiente manera:

Gana uno de los equipos
![](../../../../Users/ricar/OneDrive/Escritorio/Ingerniería%20en%20Sistemas/1er%20Año/Algoritmos%20y%20Estructuras%20de%20Datos/Clases/tablero_futbol/animaciones/Gana_local.gif)

Empatan
![](../../../../Users/ricar/OneDrive/Escritorio/Ingerniería%20en%20Sistemas/1er%20Año/Algoritmos%20y%20Estructuras%20de%20Datos/Clases/tablero_futbol/animaciones/Empate.gif)

El usuario elige la opción 4 para salir.

![](../../../../Users/ricar/OneDrive/Escritorio/Ingerniería%20en%20Sistemas/1er%20Año/Algoritmos%20y%20Estructuras%20de%20Datos/Clases/tablero_futbol/animaciones/Termina_con_Salir.gif)
