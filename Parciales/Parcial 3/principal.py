import os

from logica import carga_random, crear_lista_juicios_mayor_monto, crear_lista_juicios_por_tipo, modificar_juicio


def mostrar_menu():
    print("""a. Cargar datos de los juicios.
b. Mostrar juicios con monto mayor al sugerido.
c. Mostrar cantidad de juicios por tipo.
d. Modificar honorarios de juicio según código de expediente.
e. Salir.
""")


def pedir_opcion():
    mostrar_menu()
    opcion = input("Elija una opción: ")
    while opcion not in "abcde":
        opcion = input("Por favor, elija una opción válida: ")

    return opcion


def mostrar_datos_juicios(lista, monto):
    for i in range(len(lista)):
        print(lista[i])

    print(f"Hay un total de {len(lista)} juicios cuyo monto es mayor a {monto}.")



"""
Iba a usar estas 3 funciones que eran muy parecidas (lo único que cambia es el mensaje). 
Así que me creo una sola mas abajo que pueda usar en todos los casos
"""
# def pedir_cantidad_juicios():
#     opcion = input("Ingrese la cantidad de juicios que desea cargar: ")
#     while not opcion.isdigit():
#         print("Ingrese un número entero.")
#         opcion = input("Ingrese la cantidad de juicios que desea cargar: ")
#
#     return int(opcion)


# def pedir_cantidad():
#     opcion = input("Ingrese la cantidad mínima para mostrar el tipo de juicio: ")
#     while not opcion.isdigit():
#         print("Ingrese un número entero.")
#         opcion = input("Ingrese la cantidad mínima para mostrar el tipo de juicio: ")
#
#     return int(opcion)

# def pedir_codigo():
#     opcion = input("Ingrese el código del juicio que desea modificar: ")
#     while not opcion.isdigit():
#         print("Ingrese un número entero.")
#         opcion = input("Ingrese el código del juicio que desea modificar: ")
#
#     return int(opcion)

def pedir_numero_entero(mensaje):
    opcion = input(mensaje)
    while not opcion.isdigit():
        print("Ingrese un número entero.")
        opcion = input(mensaje)

    return int(opcion)


def mostrar_juicios_por_tipo(lista, cantidad):
    for i in range(len(lista)):
        if lista[i] > cantidad:
            print(f"Hay {lista[i]} envíos del tipo {i + 1}.")


def principal():
    opcion = pedir_opcion()
    juicios = []

    while opcion in "abcd":
        if opcion == "a":
            """Enunciado (a)"""
            # Le pido al usuario que ingrese cuántos juicios va a cargar
            cantidad_juicios = pedir_numero_entero("Ingrese la cantidad de juicios que desea cargar: ")
            # Le pido al usuario que cargue todos los juicios que dijo
            carga_random(juicios, cantidad_juicios)

        elif opcion == "b":
            # Le pido al usuario que ingrese el monto de honorarios a comparar
            monto = float(input("Ingrese un monto de honorarios"))
            # Creo una lista ordenadada cuyo monto sea mayor al especificado
            juicios_mayor_monto = crear_lista_juicios_mayor_monto(juicios, monto)
            # Muestro los datos de todos los juicios de la lista creada y la cantidad de juicios mostrada
            mostrar_datos_juicios(juicios_mayor_monto, monto)

        elif opcion == "c":
            # Le pido al usuario que ingrese la cantidad mínima de envíos por tipo que desea ver
            cantidad = pedir_numero_entero("Ingrese la cantidad mínima para mostrar el tipo de juicio: ")
            # Creo una lista que contiene la cantidad de juicios por tipo de envío
            juicios_por_tipo = crear_lista_juicios_por_tipo(juicios)
            # Muestro la cantidad de juicios que hay por cada tipo distinto para todos los tipo cuya cantidad sea mayor
            # a la pedida
            mostrar_juicios_por_tipo(juicios_por_tipo, cantidad)

        elif opcion == "d":
            # Le pido al usuario que ingrese el código de expediente del juicio que desea modificar
            codigo = pedir_numero_entero("Ingrese el código del juicio que desea modificar: ")
            juicio = modificar_juicio(juicios, codigo)
            if juicio is None:
                # Si no se encontró el juicio con el código ingresado, avisamos.
                print("El código ingresado no coincide con ningún juicio cargado.")
            else:
                # Si encontramos el juicio, modificamos su honorario
                print(juicio)

        opcion = pedir_opcion()


if __name__ == '__main__':
    principal()