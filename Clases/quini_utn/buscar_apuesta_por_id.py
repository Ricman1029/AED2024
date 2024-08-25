from otras_funciones import mostrar_titulo
from top_numeros_apostados import crear_historico_apuestas
from funciones_de_listas import buscar_en_lista
from grilla import grilla


def buscar_id(id):
    apuestas = crear_historico_apuestas(False)
    largo = len(apuestas)
    i = 0
    while i < largo and not buscar_en_lista(id, apuestas[i]):
        i += 1

    return apuestas[i]


def mostrar_apuesta_por_id(id, apuesta):
    carta = f"""
Apuesta Nro {id}
"""
    print(carta)

    columna = [["ID", 10, "<"], ["NRO1", 5, "<"], ["NRO2", 5, "<"],
               ["NRO3", 5, "<"], ["NRO4", 5, "<"], ["NRO5", 5, "<"], ["NRO6", 5, "<"]]
    grilla(columna, [apuesta])


def buscar_apuesta_por_id():
    mostrar_titulo("Buscar apuesta por identificador")

    id = int(input("Ingrese el identificador de la apuesta: "))

    apuesta = buscar_id(id)
    mostrar_apuesta_por_id(id, apuesta)


if __name__ == '__main__':
    buscar_apuesta_por_id()
