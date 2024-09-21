import os


def limpiar_pantalla():
    os.system("cls")


def crear_borde(posicion, columnas):
    if posicion == "superior":
        derecha = "┌"
        union = "┬"
        izquierda = "┐"
    elif posicion == "medio":
        derecha = "├"
        union = "┼"
        izquierda = "┤"
    elif posicion == "inferior":
        derecha = "└"
        union = "┴"
        izquierda = "┘"
    else:
        print("Opción de borde no válida.")
        return None

    borde = derecha
    for i in range(columnas):
        if i > 0:
            borde += union
        borde += "─────"
    borde += izquierda
    return borde


def mostrar_tablero(tablero):
    limpiar_pantalla()

    superior =  crear_borde("superior", len(tablero[0]))
    medio =     crear_borde("medio", len(tablero[0]))
    inferior =  crear_borde("inferior", len(tablero[0]))

    filas = len(tablero)
    columnas = len(tablero[0])

    print(superior)
    for i in range(filas):
        for j in range(columnas):
            print("│", end="")
            print(f"{tablero[i][j]:{"^"}{5}}", end="")
        print("│")

        if i < filas - 1:
            print(medio)
    print(inferior)
