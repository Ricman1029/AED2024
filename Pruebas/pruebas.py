#
def menor_mayor(x, y):
    return x < y
#
#
def mayor_menor(x, y):
    return x > y
#
#
# def ordenar_lista_esteroides(listas, indice, esta_ordenado):
#     listas1 = listas
#     largo = len(listas1)
#     i = 0
#     while i < largo:
#         j = i + 1
#         while j < largo:
#             if not esta_ordenado(int(listas1[i][indice]), int(listas1[j][indice])):
#                 listas1[i], listas1[j] = listas1[j], listas1[i]
#             j += 1
#         i += 1
#
#     return listas1
#
#
lista_original = [(7, 3), (3, 5), (2, 0), (10, 5), (6, 2)]
lista = list(lista_original)
# ordenar_lista_esteroides(lista, 0, mayor_menor)
# print(lista)
# lista = list(lista_original)
# ordenar_lista_esteroides(lista, 0, menor_mayor)
# print(lista)


def tupla_0(tupla):
    return tupla[0]


# def ordenar_lista_esteroides(listas, valor_func, esta_ordenado):
#     listas1 = listas
#     largo = len(listas1)
#     i = 0
#     while i < largo:
#         j = i + 1
#         while j < largo:
#             if not esta_ordenado(int(valor_func(listas1[i])), int(valor_func(listas1[j]))):
#                 listas1[i], listas1[j] = listas1[j], listas1[i]
#             j += 1
#         i += 1
#
#     return listas1


def ordenar_lista_esteroides(listas, esta_ordenado):
    listas1 = listas
    largo = len(listas1)
    i = 0
    while i < largo:
        j = i + 1
        while j < largo:
            if not esta_ordenado(listas1[i], listas1[j]):
                listas1[i], listas1[j] = listas1[j], listas1[i]
            j += 1
        i += 1

    return listas1


def menor_mayor_tupla(x, y):
    return x[0] < y[0] or (x[0] == y[0] and x[1] < y[1])


lista_original = [(7, 3), (10, 6), (3, 5), (2, 0), (10, 5), (6, 2), (2, 1)]
lista = list(lista_original)
ordenar_lista_esteroides(lista, menor_mayor_tupla)
print(lista)