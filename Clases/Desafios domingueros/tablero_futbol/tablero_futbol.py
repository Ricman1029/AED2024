def pedir_opcion(tiempo, nombre_local, nombre_visitante, goles_local, goles_visitante):
    if tiempo == 1:
        menu = "PRIMER TIEMPO \n" \
               f"Equipo Local: {nombre_local} - {goles_local}\n" \
               f"Equipo visitante: {nombre_visitante} - {goles_visitante}\n\n" \
               "1. Gol Local\n" \
               "2. Gol Visitante\n" \
               "3. Terminó el primer tiempo\n" \
               "4. Salir\n" \
               "Ingrese una opción: "
    else:
        menu = "SEGUNDO TIEMPO \n" \
               f"Equipo Local: {nombre_local} - {goles_local}\n" \
               f"Equipo visitante: {nombre_visitante} - {goles_visitante}\n\n" \
               "1. Gol Local\n" \
               "2. Gol Visitante\n" \
               "3. Terminó el partido\n" \
               "4. Salir\n" \
               "Ingrese una opción: "

    # opcion = -1
    # while opcion < 1 or opcion > 4:
    #     opcion = input(menu)
    #     if opcion < "1" or opcion > "4":
    #         print("Error. Se pide que elija una opción entre 1 y 4")
    #
    # return opcion
    return menu


def primer_tiempo(nombre_local, nombre_visitante):
    goles_local = goles_visitante = 0

    opcion = input(pedir_opcion(1, nombre_local, nombre_visitante, goles_local, goles_visitante))
    while opcion != "4":
        if opcion == "1":
            goles_local += 1
        elif opcion == "2":
            goles_visitante += 1
        else:
            return 3, goles_local, goles_visitante

        opcion = input(pedir_opcion(1, nombre_local, nombre_visitante, goles_local, goles_visitante))


def segundo_tiempo(nombre_local, nombre_visitante, goles_local, goles_visitante):
    opcion = input(pedir_opcion(2, nombre_local, nombre_visitante, goles_local, goles_visitante))
    while opcion != "4":
        if opcion == "1":
            goles_local += 1
        elif opcion == "2":
            goles_visitante += 1
        else:
            return 3, goles_local, goles_visitante

        opcion = input(pedir_opcion(2, nombre_local, nombre_visitante, goles_local, goles_visitante))


equipo_local = input("Ingrese el nombre del equipo local: ")
equipo_visitante = input("Ingrese el nombre del equipo visitante: ")

resultados_primer_tiempo = primer_tiempo(equipo_local, equipo_visitante)

if resultados_primer_tiempo[0] == 3:
    resultados_segundo_tiempo = segundo_tiempo(equipo_local, equipo_visitante,
                                               resultados_primer_tiempo[1], resultados_primer_tiempo[2])

    if resultados_segundo_tiempo[0] == 3:
        goles_local = resultados_primer_tiempo[1] + resultados_segundo_tiempo[1]
        goles_visitante = resultados_primer_tiempo[2] + resultados_segundo_tiempo[2]
        goles_totales = goles_local + goles_visitante
        goles_primer_tiempo = resultados_primer_tiempo[1] + resultados_primer_tiempo[2]
        goles_segundo_tiempo = goles_totales - goles_primer_tiempo

        print(f"Cantidad de goles TOTALES: {goles_totales}")
        print(f"Cantidad de goles PRIMER TIEMPO: {goles_primer_tiempo}")
        print(f"Cantidad de goles SEGUNDO TIEMPO: {goles_segundo_tiempo}")
        if goles_local > goles_visitante:
            print(f"{equipo_local} le ganó a {equipo_visitante} por {goles_local} a {goles_visitante}")
        elif goles_local < goles_visitante:
            print(f"{equipo_visitante} le ganó a {equipo_local} por {goles_visitante} a {goles_local}")
        else:
            print(f"{equipo_local} y {equipo_visitante} empataron con {goles_local} goles cada uno")

if resultados_primer_tiempo == 4 or resultados_segundo_tiempo == 4:
    print("Salió sin finalizar el partido.")

