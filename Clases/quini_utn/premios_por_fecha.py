from otras_funciones import formato_fecha, mostrar_titulo
from funciones_de_listas import (partir_cadena, buscar_coincidencias, buscar_en_lista,
                                 remover_de_lista, orden_parcial, convertir_lista_cadena)


def buscar_fecha(archivo, fecha):
    linea = archivo.readline()
    lista = partir_cadena(linea, ",\n", int)
    while linea != "" and not buscar_en_lista(int(fecha), lista):
        linea = archivo.readline()
        lista = partir_cadena(linea, ",\n", int)

    return lista


def obtener_numeros_ganadores(fecha):
    with open("datos/sorteos.txt") as archivo:
        numeros_ganadores = buscar_fecha(archivo, fecha)
    numeros_ganadores = orden_parcial(numeros_ganadores, 1, len(numeros_ganadores))

    return numeros_ganadores


def contar_premios(aciertos, uno, dos, tres):
    if aciertos == 6:
        return uno + 1, dos, tres
    if aciertos == 5:
        return uno, dos + 1, tres
    if aciertos == 4:
        return uno, dos, tres + 1
    return uno, dos, tres


def obtener_datos_del_dia(archivo, ganadores):
    primeros = segundos = terceros = cant_lineas = 0

    linea = archivo.readline()
    while linea != "":
        lista = partir_cadena(linea, ",\n", int)
        lista = orden_parcial(lista, 1, len(lista))
        aciertos = buscar_coincidencias(lista, ganadores, 1, len(ganadores))
        primeros, segundos, terceros = contar_premios(aciertos, primeros, segundos, terceros)

        cant_lineas += 1
        linea = archivo.readline()

    recaudacion = cant_lineas * 3000

    return primeros, segundos, terceros, recaudacion


def existe_ganador(numero):
    if numero > 0:
        return 0
    return 1


def calcular_vacante(importes, primeros, segundos, terceros):
    return (importes[0] * existe_ganador(primeros) +
            importes[1] * existe_ganador(segundos) +
            importes[2] * existe_ganador(terceros))


def calcular_premios_fecha(fecha):
    ganadores = obtener_numeros_ganadores(fecha)

    with open(f"datos/apuestas_{fecha}.txt") as archivo:
        primeros, segundos, terceros, recaudacion = obtener_datos_del_dia(archivo, ganadores)

    pozo = recaudacion * 0.9
    importes = (pozo * 0.7, pozo * 0.1, pozo * 0.03, pozo * 0.17)

    vacante = calcular_vacante(importes, primeros, segundos, terceros)

    numeros_ganadores = remover_de_lista(ganadores, 0, 0)
    cadena_ganadores = convertir_lista_cadena(numeros_ganadores)
    fecha = formato_fecha(fecha)
    return (recaudacion, pozo, cadena_ganadores, fecha, primeros, importes[0],
            segundos, importes[1], terceros, importes[2], importes[3], vacante)


def mostrar_premios_fecha(datos):
    carta = f"""
RECAUDACIÓN: ${datos[0]}
POZO: ${datos[1]}

Números ganadores: {datos[2]}

Premios Resultados para el {datos[3]}
1eros Premios (6 aciertos): 
    Cantidad: {datos[4]}
    Importe: ${datos[5]}
2dos Premios (5 aciertos):
    Cantidad: {datos[6]}
    Importe: ${datos[7]}
3ros Premios (4 aciertos): 
    Cantidad: {datos[8]}
    Importe: ${datos[9]}

OTRO CONCEPTOS: ${datos[10]}
VACANTE: ${datos[11]}
"""

    print(carta)


def premios_por_fecha():
    mostrar_titulo("Premios por fecha")

    fecha = input("Ingresar la fecha del sorteo (YYYYMMDD): ")
    datos_premios_fecha = calcular_premios_fecha(fecha)
    mostrar_premios_fecha(datos_premios_fecha)


if __name__ == '__main__':
    premios_por_fecha()
