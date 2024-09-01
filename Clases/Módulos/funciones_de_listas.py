def remover_de_lista(lista, inicio, fin):
    lista_final = []
    lista1 = lista[0:inicio]
    lista2 = lista[fin + 1:]

    for elemento in lista1:
        lista_final.append(elemento)

    for elemento in lista2:
        lista_final.append(elemento)

    return lista_final


def buscar_en_lista(numero, lista):
    largo = len(lista)
    i = 0
    while i < largo and numero != lista[i]:
        i += 1

    if i < largo:
        return 1
    return 0


def partir_cadena(cadena, caracteres, funcion=str):
    lista = []
    elemento = ""
    for car in cadena:
        if car not in caracteres:
            elemento += car
        else:
            lista.append(funcion(elemento))
            elemento = ""
    return lista


def selection_sort(lista):
    lista1 = lista
    largo = len(lista1)
    i = 0
    while i < largo:
        j = i + 1
        while j < largo:
            if lista1[j] < lista1[i]:
                lista1[i], lista1[j] = lista1[j], lista1[i]
            j += 1
        i += 1

    return lista1


def orden_parcial(lista, inicio, fin):
    lista1 = lista
    i = inicio
    while i < fin:
        j = i + 1
        while j < fin:
            if lista1[j] < lista1[i]:
                lista1[i], lista1[j] = lista1[j], lista1[i]
            j += 1
        i += 1

    return lista1


def ordenar_por_burbuja(lista):
    lista1 = lista
    largo = len(lista1)
    i = 0
    while i < largo:
        j = 0
        while j < largo - i - 1:
            if lista1[j] > lista1[j + 1]:
                lista1[j], lista1[j + 1] = lista1[j + 1], lista1[j]
            j += 1
        i += 1

    return lista1


def buscar_coincidencias(lista1, lista2):
    coincidencias = 0

    for elemento in lista1:
        coincidencias += buscar_en_lista(elemento, lista2)

    return coincidencias


def convertir_lista_cadena(lista):
    cadena = ""
    for elemento in lista:
        cadena += str(elemento) + " "

    return cadena


def elementos_str_int(lista):
    lista1 = lista

    for i in range(len(lista)):
        lista[i] = int(lista[i])

    return lista1


def ordenar_lista_2_dim(listas, indice, orden="a"):
    listas1 = listas
    largo = len(listas1)
    i = 0
    while i < largo:
        j = i + 1
        while j < largo:
            if orden == "a":
                if int(listas1[j][indice]) < int(listas1[i][indice]):
                    listas1[i], listas1[j] = listas1[j], listas1[i]
            elif orden == "d":
                if int(listas1[j][indice]) > int(listas1[i][indice]):
                    listas1[i], listas1[j] = listas1[j], listas1[i]
            j += 1
        i += 1

    return listas1


def ordenar_lista_esteroides(listas, esta_ordenado):
    largo = len(listas)
    i = 0
    while i < largo:
        j = i + 1
        while j < largo:
            if not esta_ordenado(listas[i], listas[j]):
                listas[i], listas[j] = listas[j], listas[i]
            j += 1
        i += 1

    return listas


def buscar_indice(valor, lista):
    largo = len(lista)
    i = 0
    while i < largo and lista[i] != valor:
        i += 1

    return i if i < largo else None


def insertar_en_lista(elemento, lista, indice=0):
    lista_nueva = []
    for i in range(indice):
        lista_nueva.append(lista[i])
    lista_nueva.append(elemento)
    for i in range(indice, len(lista)):
        lista_nueva.append(lista[i])

    return lista_nueva



if __name__ == '__main__':
    cadena = "1,2,3,4,5,6,7,8,9"
    lista = partir_cadena(cadena, ",\n", int)
    print(lista)

