import os
from logica import (generar_equipos, carga_manual, ejecutar_opcion_1, ejecutar_opcion_2, ejecutar_opcion_3,
                    ejecutar_opcion_4, ejecutar_opcion_5)


def limpiar_pantalla():
    os.system('cls')


def mostrar_menu():
    limpiar_pantalla()
    print('''1. Tabla de posiciones.
2. Punteros.
3. Tabla de Descenso.
4. Mejor desempeno.
5. Comparativo.
6. Salir.''')


def mostrar_titulo():
    limpiar_pantalla()
    print("Este programa simula un torneo de futbol")
    print("----------------------------------------")


def elegir_opcion(mensaje, opciones_validas):
    opcion = int(input(mensaje))
    while opcion not in opciones_validas:
        print('Opcion no valida.')
        opcion = int(input(mensaje))

    return opcion


def cargar_datos_equipos():
    print("Opciones de carga.\n1. Automática.\n2. Manual")
    opcion = elegir_opcion("Ingrese una opción: ", (1, 2))
    if opcion == 1:
        cantidad_equipos = elegir_opcion("Ingrese la cantidad de equipos que desea agregar: ", range(1, 13))
        return generar_equipos(cantidad_equipos)
    else:
        return carga_manual()


def principal():
    mostrar_titulo()
    equipos = cargar_datos_equipos()
    mostrar_menu()
    opcion = elegir_opcion("Ingrese una opción: ", (1, 2, 3, 4, 5, 6))
    while opcion in (1, 2, 3, 4, 5):
        if opcion == 1:
            ejecutar_opcion_1(equipos)
        input("Presione 'ENTER' para continuar")
        mostrar_menu()
        opcion = elegir_opcion("Ingrese una opción: ", (1, 2, 3, 4, 5, 6))



if __name__ == '__main__':
    principal()