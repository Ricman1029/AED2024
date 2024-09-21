import os
import random

from dominio import Juicio


def limpiar_pantalla():
    os.system("cls")


"""Enunciado (a)"""
def ingresar_codigo():
    opcion = input("Ingrese el código de expediente (número entero): ")
    while not opcion.isdigit():
        print("El código ingresado no es un número entero.")
        opcion = input("Ingrese el código de expediente (número entero): ")

    return int(opcion)


def ingresar_tipo():
    opcion = input("Ingrese el tipo de juicio (número entero entre 1 y 15): ")
    while not opcion.isdigit() or not 1 <= int(opcion) <= 15:
        print("El tipo ingresado no es un número entero entre 1 y 15.")
        opcion = input("Ingrese el tipo de juicio (número entero entre 1 y 15): ")

    return int(opcion)


def cargar_juicios(lista, cantidad):
    for i in range(cantidad):
        limpiar_pantalla()
        codigo = ingresar_codigo()
        descripcion = input("Ingrese la descripción: ")
        tipo = ingresar_tipo()
        cliente = input("Ingrese el nombre del cliente: ")
        honorarios = float(input("Ingrese el monto de honorarios a cobrar: "))
        juicio = Juicio(codigo, descripcion, tipo, cliente, honorarios)
        lista.append(juicio)


def carga_random(lista, cantidad):
    for i in range(cantidad):
        codigo = random.randint(10000, 100000)
        descripcion = random.choice("abcdefghijklmnopqrstuvwxyz")
        tipo = random.randint(1, 15)
        cliente = "cliente"
        honorarios = random.randrange(5000, 50000)
        juicio = Juicio(codigo, descripcion, tipo, cliente, honorarios)
        lista.append(juicio)

    return lista


"""Enunciado (b)"""
def ordenar_lista(lista):
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i].descripcion > lista[j].descripcion:
                lista[i], lista[j] = lista[j], lista[i]


def crear_lista_juicios_mayor_monto(lista, monto):
    nueva_lista = []
    for i in range(len(lista)):
        if lista[i].honorarios > monto:
            nueva_lista.append(lista[i])
    ordenar_lista(nueva_lista)

    return nueva_lista


"""Enunciado (c)"""
def crear_lista_juicios_por_tipo(lista):
    vector_conteo = [0] * 15
    for i in range(len(lista)):
        # Pongo .tipo - 1 porque el tipo de envío va del 1 al 15, pero las posiciones van del 0 al 14
        vector_conteo[lista[i].tipo - 1] += 1

    return vector_conteo


"""Enunciado (d)"""
def indice_juicio(lista, codigo):
    largo = len(lista)
    i = 0
    while i < largo and lista[i].codigo_expediente != codigo:
        i += 1

    # Si en esta línea i es igual a largo quiere decir que recorrimos toda la lista y no encontramos un juicio que
    # tenga el mismo código que el que se ingresó por teclado así que devolvemos None.
    # PERO si i es menor que largo quiere decir que encontramos el juicio y entonces devolvemos su índice en la lista
    return i if i < largo else None


def modificar_juicio(lista, codigo):
    indice = indice_juicio(lista, codigo)

    if indice is not None:
        # Encontramos el juicio asi que modificamos sus honorarios
        lista[indice].honorarios = float(input("Ingrese el monto de honorarios a cobrar: "))
        # Devolvemos el juicio modificado
        return lista[indice]

    # Si no encontramos el juicio, devolvemos None
    return None
