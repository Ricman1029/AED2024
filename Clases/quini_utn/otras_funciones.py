import os


def limpiar_pantalla():
    os.system("cls")


def formato_fecha(cadena):
    return f"{cadena[6:]}/{cadena[4:6]}/{cadena[0:4]}"


def mostrar_titulo(titulo):
    limpiar_pantalla()
    print(titulo)
    print("—" * len(titulo))
    print()


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