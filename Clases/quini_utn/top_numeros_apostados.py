import glob
from otras_funciones import mostrar_titulo, obtener_todas_las_apuestas
from funciones_de_listas import partir_cadena, remover_de_lista, ordenar_lista_esteroides
from grilla import grilla


def contar_apariciones_numeros(historial_apuestas):
    control = [(0, 0)] * 46
    apuestas = obtener_todas_las_apuestas(historial_apuestas)

    for apuesta in apuestas:
        for i in range(len(apuesta.numeros)):
            apariciones = control[apuesta.numeros[i]][1]
            control[apuesta.numeros[i]] = (apuesta.numeros[i], apariciones + 1)

    return control


def armar_lista_top_apostados(lista, cantidad):
    top_apostados = [0] * cantidad
    for i in range(cantidad):
        top_apostados[i] = (i + 1, lista[i][0], lista[i][1])

    return top_apostados


def mostrar_top_apostados(cadena, numeros, cantidad):
    carta = f"""
Los {cantidad} numeros {cadena} apostados son: 
"""
    print(carta)

    columnas = [["#", 4, ">"], ["NRO", 4, ">"], ["CANTIDAD", 10, ">"]]
    grilla(columnas, numeros)


def numeros_mas_apostados(quini):
    mostrar_titulo("Números más apostados")

    cantidad = int(input("Ingrese la cantidad de números que desea ver: "))

    aparciciones = contar_apariciones_numeros(quini.historial_apuestas)
    apariciones_ordenadas = ordenar_lista_esteroides(aparciciones, lambda x, y: x[1] > y[1])
    lista_de_numeros = armar_lista_top_apostados(apariciones_ordenadas, cantidad)

    mostrar_top_apostados("mas", lista_de_numeros, cantidad)


def numeros_menos_apostados(quini):
    mostrar_titulo("Números menos apostados")

    cantidad = int(input("Ingrese la cantidad de números que desea ver: "))

    aparciciones = contar_apariciones_numeros(quini.historial_apuestas)
    apariciones_ordenadas = ordenar_lista_esteroides(aparciciones, lambda x, y: x[1] < y[1])
    lista_de_numeros = armar_lista_top_apostados(apariciones_ordenadas, cantidad)

    mostrar_top_apostados("menos", lista_de_numeros, cantidad)


if __name__ == '__main__':
    numeros_mas_apostados()
