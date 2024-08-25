import glob
from otras_funciones import mostrar_titulo
from funciones_de_listas import partir_cadena, remover_de_lista, ordenar_lista_2_dim
from grilla import grilla


def crear_historico_apuestas(remover=True):
    apuestas = []

    ubicaciones = glob.glob("datos/apuestas_*.txt")
    for ubicacion in ubicaciones:
        with open(ubicacion) as archivo:
            linea = archivo.readline()
            while linea != "":
                lista = partir_cadena(linea, ",\n", int)
                lista = remover_de_lista(lista, 0, 0) if remover else lista
                apuestas.append(lista)
                linea = archivo.readline()

    return apuestas


def contar_apariciones_numeros():
    control = [(0, 0)] * 46
    apuestas = crear_historico_apuestas()

    for apuesta in apuestas:
        for i in range(len(apuesta)):
            control[apuesta[i]] = (apuesta[i], control[apuesta[i]][1] + 1)

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


def numeros_mas_apostados():
    mostrar_titulo("Números más apostados")

    cantidad = int(input("Ingrese la cantidad de números que desea ver: "))

    aparciciones = contar_apariciones_numeros()
    apariciones_ordenadas = ordenar_lista_2_dim(aparciciones, 1, "d")
    lista_de_numeros = armar_lista_top_apostados(apariciones_ordenadas, cantidad)

    mostrar_top_apostados("mas", lista_de_numeros, cantidad)


def numeros_menos_apostados():
    mostrar_titulo("Números menos apostados")

    cantidad = int(input("Ingrese la cantidad de números que desea ver: "))

    aparciciones = contar_apariciones_numeros()
    apariciones_ordenadas = ordenar_lista_2_dim(aparciciones, 1, "a")
    lista_de_numeros = armar_lista_top_apostados(apariciones_ordenadas, cantidad)

    mostrar_top_apostados("menos", lista_de_numeros, cantidad)


if __name__ == '__main__':
    numeros_mas_apostados()
