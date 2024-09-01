"""
Generamos un tablero vacío
Mostramos el tablero
Bucle:
    Pedimos al jugador 1 que ingrese una posicion
    Actualizamos el tablero
    Chqueamos si alguien ganó
    Mostramos el tablero
    Si hay ganador o empate, finaliza el programa
    Pedimos al jugador 2 que ingrese una posicion
    Actualizamos el tablero
    Chqueamos si alguien ganó
    Mostramos el tablero
    Si hay ganador o empate, finaliza el programa
"""
import os

"""
┌─────┬─────┬─────┐
│  X  │     │     │
├─────┼─────┼─────┤
│     │     │     │
├─────┼─────┼─────┤
│     │     │     │
└─────┴─────┴─────┘
"""

ROJO = "\033[91m"
VERDE = "\033[92m"
RESET = "\033[0m"


def limpiar_pantalla():
    os.system("cls")


def generar_tablero():
    tablero = []
    for i in range(3):
        tablero.append([0] * 3)
        for j in range(3):
            tablero[i][j] = f"{3 * i + j + 1}"

    return tablero


def dibujar_lineas():
    superior =  "┌─────┬─────┬─────┐"
    medio =     "├─────┼─────┼─────┤"
    inferior =  "└─────┴─────┴─────┘"

    return superior, medio, inferior


def pintar_verde(texto):
    print(f"{VERDE}{texto}{RESET}", end='')


def pintar_rojo(texto):
    print(f"{ROJO}{texto}{RESET}", end='')


def colorear(valor):
    if valor == "X":
        pintar_verde(f"  {valor}  ")
    elif valor == "O":
        pintar_rojo(f"  {valor}  ")
    else:
        print(f"  {valor}  ", end="")


def mostrar_tablero(lista):
    limpiar_pantalla()

    superior, medio, inferior = dibujar_lineas()
    print(superior)

    for i in range(3):
        for j in range(3):
            print("│", end="")
            colorear(lista[i][j])
        print("│")

        if i < 2:
            print(medio)

    print(inferior)


def hay_ganador(tablero):
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
            print(f"Gana '{tablero[i][0]}'")
            return True

    for i in range(3):
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
            print(f"Gana '{tablero[0][i]}'")
            return True

    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " " or tablero[2][0] == tablero[1][1] == tablero[0][2] != " ":
        print(f"Gana '{tablero[1][1]}'")
        return True

    return False


def tablero_lleno(tablero):
    for fila in tablero:
        for valor in fila:
            if valor != "X" and valor != "O":
                return False
    print("Empate")
    return True


def fin_juego(tablero):
    return hay_ganador(tablero) or tablero_lleno(tablero)


def pedir_jugada(jugador, posibilidades):
    opcion = -1
    while opcion not in posibilidades:
        opcion = int(input(f"Jugador {jugador}: "))

    posibilidades.remove(opcion)
    return opcion


def modificar_tablero(tablero, posicion, valor):
    posiciones = ((0, 0), (0, 1), (0, 2),
                  (1, 0), (1, 1), (1, 2),
                  (2, 0), (2, 1), (2, 2))

    fila = posiciones[posicion][0]
    columna = posiciones[posicion][1]
    tablero[fila][columna] = valor


def empezar_juego(tablero):
    posiciones_disponibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    jugadores = ("X", "O")
    turno = 0
    jugador = jugadores[turno]
    while not fin_juego(tablero):
        posicion = pedir_jugada(turno, posiciones_disponibles)
        modificar_tablero(tablero, posicion - 1, jugador)
        mostrar_tablero(tablero)
        turno = turno ^ 1
        jugador = jugadores[turno]


def principal():
    tablero = generar_tablero()
    mostrar_tablero(tablero)
    empezar_juego(tablero)


if __name__ == '__main__':
    principal()
