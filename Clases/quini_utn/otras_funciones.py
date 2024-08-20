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
