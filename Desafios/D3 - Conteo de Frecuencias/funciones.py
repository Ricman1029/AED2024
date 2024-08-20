def buscar_indice(lista, valor):
    largo = len(lista)
    i = 0
    while i < largo and lista[i] != valor:
        i += 1

    return i if i < largo else None


def ordenar_lista(lista):
    salida = lista[:]
    largo = len(salida)
    for i in range(largo - 1):
        for j in range(i + 1, largo):
            if salida[i] < salida[j]:
                salida[i], salida[j] = salida[j], salida[i]

    return salida