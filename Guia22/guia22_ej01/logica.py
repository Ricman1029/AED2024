import random

from entidades import Equipo
from muestra_datos import mostrar_equipos_ordenados


def generar_equipos(cantidad):
    nombres = ["Boca", "River", "Independiente", "Estudiantes", "Gimnasia", "San Lorenzo", "Racing",
               "Defensa y Justicia", "Chacaritas", "Tigre", "Talleres", "Colon"]
    equipos = []

    for i in range(cantidad):
        nombre = random.choice(nombres)
        nombres.remove(nombre)
        goles = random.randint(0, 30)
        puntos =  random.randint(0, 20)
        equipo = Equipo(nombre, goles, puntos)
        equipos.append(equipo)

    return equipos


def carga_manual():
    equipos = []
    nombre = input("Ingrese el nombre del equipo: ")
    goles = int(input("Ingrese la cantidad de goles del equipo: "))
    puntos = int(input("Ingrese la canteidad de puntos del equipo: "))
    equipo = Equipo(nombre, goles, puntos)
    equipos.append(equipo)


def ordenar_por_puntaje(equipos):
    nueva_lista_equipos = equipos[0:len(equipos)]
    for i in range(len(nueva_lista_equipos) - 1):
        for j in range(i + 1, len(nueva_lista_equipos)):
            if nueva_lista_equipos[i].puntos > nueva_lista_equipos[j].puntos:
                nueva_lista_equipos[i], nueva_lista_equipos[j] = nueva_lista_equipos[j], nueva_lista_equipos[i]
    return nueva_lista_equipos


def ejecutar_opcion_1(equipos):
    equipos_ordenados = ordenar_por_puntaje(equipos)
    mostrar_equipos_ordenados(equipos_ordenados)


def ejecutar_opcion_2():
    pass


def ejecutar_opcion_3():
    pass


def ejecutar_opcion_4():
    pass


def ejecutar_opcion_5():
    pass
