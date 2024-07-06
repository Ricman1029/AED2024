import os


def mostrar_tablero1(local, visitante, goles_local, goles_visitante):
    os.system("cls")

    tablero = ("PRIMER TIEMPO\n"
               f"Equipo Local: {local} - {goles_local}\n"
               f"Equipo visitante: {visitante} - {goles_visitante}\n\n"
               "1. Gol Local\n"
               "2. Gol Visitante\n"
               "3. Terminó el primer tiempo\n"
               "4. Salir\n"
               "Ingrese una opción: ")

    opcion = input(tablero)
    return opcion


def mostrar_tablero2(local, visitante, goles_local, goles_visitante):
    os.system("cls")

    tablero = ("SEGUNDO TIEMPO\n"
               f"Equipo Local: {local} - {goles_local}\n"
               f"Equipo visitante: {visitante} - {goles_visitante}\n\n"
               "1. Gol Local\n"
               "2. Gol Visitante\n"
               "3. Terminó el partido\n"
               "4. Salir\n"
               "Ingrese una opción: ")

    opcion = input(tablero)
    return opcion


def actualizar_goles(gol, local, visitante):
    if gol == "1":
        local += 1
    elif gol == "2":
        visitante += 1

    return local, visitante


def mostrar_resultados(opcion, local, visitante, goles_local, goles_visitante):
    os.system("cls")

    if opcion == "4":
        print("Salió sin finalizar el partido.")
    elif goles_local > goles_visitante:
        print(f"{local} le ganó a {visitante} por {goles_local} a {goles_visitante}")
    elif goles_local < goles_visitante:
        print(f"{visitante} le ganó a {local} por {goles_visitante} a {goles_local}")
    else:
        print(f"{local} y {visitante} empataron con {goles_local} goles cada uno")


def simular_partido(local, visitante):
    es_primer_tiempo = True
    goles_local = goles_visitante = 0

    opcion = mostrar_tablero1(local, visitante, goles_local, goles_visitante)
    while opcion != "4":
        if opcion != "3":
            # Primer tiempo
            if es_primer_tiempo:
                goles_local, goles_visitante = actualizar_goles(opcion, goles_local, goles_visitante)
                opcion = mostrar_tablero1(local, visitante, goles_local, goles_visitante)
            # Segundo tiempo
            else:
                goles_local, goles_visitante = actualizar_goles(opcion, goles_local, goles_visitante)
                opcion = mostrar_tablero2(local, visitante, goles_local, goles_visitante)
        else:
            if not es_primer_tiempo:
                return opcion, goles_local, goles_visitante
            es_primer_tiempo = False
            opcion = mostrar_tablero2(local, visitante, goles_local, goles_visitante)

    return opcion, goles_local, goles_visitante


def principal():
    equipo_local = input("Ingrese el nombre del equipo local: ")
    equipo_visitante = input("Ingrese el nombre del equipo visitante: ")

    opcion, goles_local, goles_visitante = simular_partido(equipo_local, equipo_visitante)

    mostrar_resultados(opcion, equipo_local, equipo_visitante, goles_local, goles_visitante)


if __name__ == "__main__":
    principal()
