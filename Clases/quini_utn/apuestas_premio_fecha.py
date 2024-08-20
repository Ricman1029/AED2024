from otras_funciones import formato_fecha, mostrar_titulo
from premios_por_fecha import obtener_numeros_ganadores
from funciones_de_listas import (partir_cadena, orden_parcial, buscar_coincidencias,
                                 ordenar_lista_2_dim, elementos_str_int)
from grilla import grilla

def crear_lista_de_apuestas(archivo):
    apuestas = []
    linea = archivo.readline()
    while linea != "":
        apuesta = partir_cadena(linea, ",\n", int)
        apuesta = orden_parcial(apuesta, 1, len(apuesta))
        apuestas.append(apuesta)
        linea = archivo.readline()

    return apuestas


def crear_lista_ganadores_por_premio(premio, apuestas, numeros):
    ganadores = []
    largo = len(numeros)

    for apuesta in apuestas:
        aciertos = buscar_coincidencias(apuesta, numeros, 1, largo)
        if aciertos == premio:
            ganadores.append(apuesta)

    return ganadores


def obtener_apuestas_por_premio(fecha, premio):
    numeros_ganadores = obtener_numeros_ganadores(fecha)
    numeros_ganadores = orden_parcial(numeros_ganadores, 1, len(numeros_ganadores))

    with open(f"datos/apuestas_{fecha}.txt") as archivo:
        lista = crear_lista_de_apuestas(archivo)

    aciertos = 7 - premio
    lista_de_ganadores = crear_lista_ganadores_por_premio(aciertos, lista, numeros_ganadores)

    return lista_de_ganadores


def mostrar_resultados_por_premio(apuestas, premio, fecha):
    carta = f"""
Las apuestas que obtuvieron el premio {premio} para la fecha {fecha} son:
"""
    print(carta)

    columnas = [["ID", 10, "<"], ["NRO 1", 5, "<"], ["NRO 2", 5, "<"], ["NRO 3", 5, "<"],
                ["NRO 4", 5, "<"], ["NRO 5", 5, "<"], ["NRO 6", 5, "<"]]
    grilla(columnas, apuestas)


def apuestas_por_premio_por_fecha():
    mostrar_titulo("Resultados por premio por fecha")

    fecha = input("Ingresar la fecha del sorteo (YYYYMMDD): ")
    premio = int(input("Ingrese un premio (1, 2 o 3): "))

    ganadores = obtener_apuestas_por_premio(fecha, premio)
    ganadores_ordenados = ordenar_lista_2_dim(ganadores, 0)

    fecha = formato_fecha(fecha)
    mostrar_resultados_por_premio(ganadores_ordenados, premio, fecha)


if __name__ == '__main__':
    apuestas_por_premio_por_fecha()
