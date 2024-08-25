from otras_funciones import formato_fecha, mostrar_titulo
from funciones_de_listas import buscar_en_lista, convertir_lista_cadena


def obtener_numeros_ganadores(fecha, sorteos):
    largo = len(sorteos)
    i = 0
    while i < largo and sorteos[i].fecha != int(fecha):
        i += 1

    return sorteos[i].numeros


def obtener_apuestas_del_dia(fecha, historico_apuestas):
    largo = len(historico_apuestas)
    i = 0
    while i < largo and historico_apuestas[i].fecha != fecha:
        i += 1

    return historico_apuestas[i].apuestas


def contar_premios(aciertos, uno, dos, tres):
    if aciertos == 6:
        return uno + 1, dos, tres
    if aciertos == 5:
        return uno, dos + 1, tres
    if aciertos == 4:
        return uno, dos, tres + 1
    return uno, dos, tres


def obtener_datos_del_dia(apuestas, ganadores):
    primeros = segundos = terceros = 0

    for apuesta in apuestas:
        aciertos = 0
        for numero in apuesta.numeros:
            aciertos += buscar_en_lista(numero, ganadores)
        primeros, segundos, terceros = contar_premios(aciertos, primeros, segundos, terceros)

    recaudacion = len(apuestas) * 3000

    return primeros, segundos, terceros, recaudacion


def existe_ganador(numero):
    if numero > 0:
        return 0
    return 1


def calcular_vacante(importes, primeros, segundos, terceros):
    return (importes[0] * existe_ganador(primeros) +
            importes[1] * existe_ganador(segundos) +
            importes[2] * existe_ganador(terceros))


def calcular_premios_fecha(fecha, quini):
    ganadores = obtener_numeros_ganadores(fecha, quini.sorteos)
    apuestas_del_dia = obtener_apuestas_del_dia(fecha, quini.historial_apuestas)
    primeros, segundos, terceros, recaudacion = obtener_datos_del_dia(apuestas_del_dia, ganadores)

    pozo = recaudacion * 0.9
    importes = (pozo * 0.7, pozo * 0.1, pozo * 0.03, pozo * 0.17)

    vacante = calcular_vacante(importes, primeros, segundos, terceros)

    cadena_ganadores = convertir_lista_cadena(ganadores)
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


def premios_por_fecha(quini):
    mostrar_titulo("Premios por fecha")

    fecha = input("Ingresar la fecha del sorteo (YYYYMMDD): ")
    datos_premios_fecha = calcular_premios_fecha(fecha, quini)
    mostrar_premios_fecha(datos_premios_fecha)


if __name__ == '__main__':
    premios_por_fecha()
