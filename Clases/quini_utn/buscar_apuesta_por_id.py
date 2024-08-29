from otras_funciones import mostrar_titulo, obtener_todas_las_apuestas
from funciones_de_listas import insertar_en_lista, ordenar_lista_esteroides
from grilla import grilla


def buscar_id(id, historial_apuestas):
    apuestas = obtener_todas_las_apuestas(historial_apuestas)
    largo = len(apuestas)
    i = 0
    while i < largo and id != apuestas[i].id:
        i += 1

    apuesta = apuestas[i].numeros
    apuesta = ordenar_lista_esteroides(apuesta, lambda x, y: x < y)
    apuesta = insertar_en_lista(apuestas[i].id, apuesta)
    return apuesta


def mostrar_apuesta_por_id(id, apuesta):
    carta = f"""
Apuesta Nro {id}
"""
    print(carta)

    columna = [["ID", 10, "<"], ["NRO 1", 5, "<"], ["NRO 2", 5, "<"],
               ["NRO 3", 5, "<"], ["NRO 4", 5, "<"], ["NRO 5", 5, "<"], ["NRO 6", 5, "<"]]
    grilla(columna, [apuesta])


def buscar_apuesta_por_id(quini):
    mostrar_titulo("Buscar apuesta por identificador")

    id = int(input("Ingrese el identificador de la apuesta: "))

    apuesta = buscar_id(id, quini.historial_apuestas)
    mostrar_apuesta_por_id(id, apuesta)


if __name__ == '__main__':
    buscar_apuesta_por_id()
