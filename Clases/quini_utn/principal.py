import os
from premios_por_fecha import premios_por_fecha
from apuestas_premio_fecha import apuestas_por_premio_por_fecha
from top_numeros_apostados import numeros_mas_apostados, numeros_menos_apostados
from buscar_apuesta_por_id import buscar_apuesta_por_id


def limpiar_pantalla():
    os.system("cls")


def generar_menu():
    limpiar_pantalla()

    menu = '''1. Premios por fecha 
2. Apuestas por premio por fecha 
3. Números más apostados 
4. Números menos apostados 
5. Buscar apuesta por identificador 
6. Salir
Elija una opcion: '''

    return menu


def pedir_opcion():
    opcion = input(generar_menu())
    while opcion not in "123456":
        opcion = input(generar_menu())

    return int(opcion)


def ejecutar_opcion(opcion):
    if opcion == 5:
        return

    funcion = (premios_por_fecha,
               apuestas_por_premio_por_fecha,
               numeros_mas_apostados,
               numeros_menos_apostados,
               buscar_apuesta_por_id)

    funcion[opcion]()


def principal():
    opcion = pedir_opcion()

    ejecutar_opcion(opcion - 1)


if __name__ == '__main__':
    principal()
