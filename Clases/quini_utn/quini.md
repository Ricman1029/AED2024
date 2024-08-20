# Quini UTN


## Reglas del juego

Las reglas del Quini UTN son las siguientes (es una variante del quini 6 tradicional):

En el Quini UTN, el apostador puede elegir 6 números entre el 0 y 45.

El pozo para los premios se determina a partir de las apuestas realizadas. Cada apuesta tiene un costo de $3000.
El 90% de lo recaudado es destinado al pozo para los premios.
El 10% de lo recaudado es destinado a costos operativos del Quini UTN.

Durante el sorteo, se seleccionan al azar 6 números.
Los premios se reparten entre los cupones.

Primeros premios: coinciden los 6 números de la apuesta
Segundos premios: coinciden solo 5 números de la apuesta
Terceros premios: coinciden solo 4 números de la apuesta


### Distribución del pozo

El pozo para los premios se distribuye de la siguiente manera:
* el 70% se distribuye entre los primeros premios
* el 10% se distribuye entre los segundos premios
* el 3% se distribuye entre los terceros premios
* el porcentaje restante corresponde a "otros conceptos"

### Archivos

Se cuenta con dos formatos de archivos 
1. apuestas_YYYYMMDD.txt
    Hay más de un archivo. Cada uno contiene todas las apuestas realizadas para la fecha YYYYMMDD, a razón de una apuesta por fila, donde cada fila tiene el siguiente formato:
 
    ID_APUESTA,NRO_1,NRO_2,NRO_3,NRO_4,NRO_5,NRO_6

    Por ejemplo:
        56,20,32,17,7,3,40
        Donde 56 es el identificador de la apuesta y 20, 32, 17, 7, 3, 40 son los números elegidos en la apuesta.

    Notar que los números de la apuesta no tienen orden y no se repiten para una misma apuesta.


2. sorteos.txt: 
    Contiene los resultados de los sorteos por día con el siguiente formato:

    YYYYMMDD,NRO_1,NRO_2,NRO_3,NRO_4,NRO_5,NRO_6

    Donde YYYYMMDD es la fecha del sorteo y NRO_1, NRO_2, NRO_3, NRO_4, NRO_5, NRO_6 son los números que salieron sorteados para esa fecha.

    Por ejemplo:

        20241104,43,2,24,13,15,6

    Notar que los números del sorteo no tienen orden y no se repiten en el mismo sorteo


 
## El programa

Se pide un programa que muestre un menú donde el usuario pueda elegir entra las siguientes opciones:
    1. Premios por fecha
    2. Apuestas por premio por fecha
    3. Números más apostados
    4. Números menos apostados
    5. Buscar apuesta por identificador
    6. Salir

### Premios por fecha

En esta opción el usuario debe ingresar una fecha y el programa debe indicar la distribución de premios según los aciertos de las apuestas, para obtener la cantidad y el importe. También debe mostrar los número ganadores ordenados de menor a mayor:

Esta pantalla debe lucir así:
<pre style="font-family: Lucila Console, Courier New, monospace; font-size: 11pt; line-height: 1.1; ">

    Premios por fecha
    ─────────────────

    Ingresar la fecha del sorteo (YYYYMMDD): 20240516

    RECAUDACIÓN: $######,##
    POZO: $######,##

    Números ganadores: NN NN NN NN NN NN NN

    Premios Resultados para el 16/05/2024
    1eros Premios (6 aciertos): 
        Cantidad: NN
        Importe: $######,##
    2dos Premios (5 aciertos):
        Cantidad: NN
        Importe: $######,##
    3ros Premios (4 aciertos): 
        Cantidad: NNN
        Importe: $######,##

    OTRO CONCEPTOS: $#####,##
    VACANTE: $#####,##
</pre>

### Resultados por premio por fecha

En esta opción el usuario debe ingresar una fecha y un número de premio (1, 2 o 3). El programa debe mostrar todas las apuestas que corresponde a ese premio, ordenadas por número de apuesta.
Mostrar los números de las apuestas ordenados de menor a mayor.
En este ejemplo se muestra cómo debe lucir la pantalla:

<pre style="font-family: Lucila Console, Courier New, monospace; font-size: 11pt; line-height: 1.1; ">
    
    Resultados por premio por fecha
    ───────────────────────────────
    
    Ingresar la fecha del sorteo (YYYYMMDD): 20240516
    Ingrese un premio (1, 2 o 3): 3

    Las apuestas que obtuvieron el premio 3 para la fecha 16/05/2024 son:

    ╔══════╦═════╦═════╦═════╦═════╦═════╦═════╗
    ║ID    ║NRO 1║NRO 2║NRO 3║NRO 4║NRO 5║NRO 6║
    ╠══════╬═════╬═════╬═════╬═════╬═════╬═════╣
    ║    56║    6║   14║   19║   21║   24║   34║
    ╠══════╬═════╬═════╬═════╬═════╬═════╬═════╣
    ║ NNNNN║   NN║   NN║   NN║   NN║   NN║   NN║
    ╚══════╩═════╩═════╩═════╩═════╩═════╩═════╝

</pre>

### Números más apostados

Debe mostrar los primeros N números más apostados en orden descendente
El usuario debe ingresar la cantidad de números que desea ver

Esa pantalla se debe ver así:


<pre style="font-family: Lucila Console, Courier New, monospace; font-size: 11pt; line-height: 1.1; ">

    Números más apostados:
    ──────────────────────

    Ingrese la cantidad de números que desea ver: 5

    Los 5 números más apostados son:

    ╔══════╦═════╦════════╗
    ║     #║  NRO║CANTIDAD║
    ╠══════╬═════╬════════╣
    ║     1║    7║     300║
    ╠══════╬═════╬════════╣
    ║     2║   17║     122║
    ╠══════╬═════╬════════╣
    ║     3║   23║     100║
    ╠══════╬═════╬════════╣
    ║     4║   18║      87║
    ╠══════╬═════╬════════╣
    ║     5║   30║      54║
    ╚══════╩═════╩════════╝

</pre>

### Números menos apostados

Debe mostrar los primeros N números menos apostados en orden ascendente
El usuario debe ingresar la cantidad de números que desea ver

Esa pantalla se debe ver así:


<pre style="font-family: Lucila Console, Courier New, monospace; font-size: 11pt; line-height: 1.1; ">

    Números menos apostados:
    ────────────────────────

    Ingrese la cantidad de números que desea ver: 5

    Los 5 números menos apostados son:

    ╔══════╦═════╦════════╗
    ║     #║  NRO║CANTIDAD║
    ╠══════╬═════╬════════╣
    ║     1║    0║       1║
    ╠══════╬═════╬════════╣
    ║     2║    1║       2║
    ╠══════╬═════╬════════╣
    ║     3║   20║       5║
    ╠══════╬═════╬════════╣
    ║     4║   14║       5║
    ╠══════╬═════╬════════╣
    ║     5║   19║       7║
    ╚══════╩═════╩════════╝

</pre>

### Buscar apuesta por identificador

Debe mostrar la apuesta que se corresponde con un identificador que debe proveer el usuario. 
Mostrar los número ordenados de menor a mayor

<pre style="font-family: Lucila Console, Courier New, monospace; font-size: 11pt; line-height: 1.1; ">

    Buscar apuesta por identificador:
    ─────────────────────────────────

    Ingrese el identificador de la apuesta: 56

    Apuesta Nro 56

    ╔══════╦═════╦═════╦═════╦═════╦═════╦═════╗
    ║ID    ║NRO 1║NRO 2║NRO 3║NRO 4║NRO 5║NRO 6║
    ╠══════╬═════╬═════╬═════╬═════╬═════╬═════╣
    ║    56║    6║   14║   19║   21║   24║   34║
    ╚══════╩═════╩═════╩═════╩═════╩═════╩═════╝

</pre>