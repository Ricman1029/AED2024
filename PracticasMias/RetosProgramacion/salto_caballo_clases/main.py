import os
import time

from consola import mostrar_tablero
from entidades import Tablero


def limpiar_pantalla():
    os.system("cls")


def pedir_opcion(opciones, mensaje):
    opcion = int(input(mensaje))
    while opcion not in opciones:
        print("Opción inválida.")
        opcion = int(input(mensaje))
    return opcion


def modo_automatico():
    pass


def modo_manual():
    input("Presion 'ENTER' para continuar.")


def preguntar_modo():
    limpiar_pantalla()
    mensaje = """1. Modo de visualización automático.
2. Modo de visuzalización manual.

Elija una opción: """
    modo = pedir_opcion((1, 2), mensaje)
    if modo == 1:
        return modo_automatico
    return modo_manual


def main():
    modo_visualizacion = preguntar_modo()

    limpiar_pantalla()
    filas = int(input("Filas: "))
    columnas = int(input("Columnas: "))
    posicion_inicial = input("Indique la posición en la que desea empezar ('fila,columna'): ")
    t_inicial = time.time()
    tablero = Tablero(filas, columnas, posicion_inicial)
    mostrar_tablero(tablero.tablero, tablero.movimiento)

    while tablero.siguiente_salto() is not None:
        tablero.saltar()
        mostrar_tablero(tablero.tablero, tablero.movimiento)
        modo_visualizacion()

    t_final = time.time()
    print(t_final - t_inicial)


if __name__ == '__main__':
    main()