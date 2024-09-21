import os


def limpiar_pantalla():
    os.system("cls")


def preguntar_modo():
    mensaje = """Modo de visualización automático (1)
Modo de visuzalización manual. (!= 1)

Elija una opción: """
    modo = input(mensaje)
    limpiar_pantalla()
    if modo == "1":
        return "Automático"
    return "Manual"


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


def pintar_color(color, valor):
    rojo = "\033[91m"
    verde = "\033[92m"
    reset = "\033[0m"
    if color == "rojo":
        color = rojo
    else:
        color = verde

    print(f"{color}{valor:{"^"}{5}}{reset}", end="")


def mostrar_tablero(tablero, ultimo_ingresado):
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
            if tablero[i][j] == ultimo_ingresado:
                pintar_color("rojo", tablero[i][j])
            elif tablero[i][j] == 1:
                pintar_color("verde", tablero[i][j])
            else:
                print(f"{tablero[i][j]:{"^"}{5}}", end="")
        print("│")

        if i < filas - 1:
            print(medio)
    print(inferior)
