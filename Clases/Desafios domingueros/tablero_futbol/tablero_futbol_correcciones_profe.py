import os

def limpiar_pantalla():
    os.system("cls")
    
def mostrar_tablero(es_primer_tiempo, local, visitante, goles_local, goles_visitante):
    limpiar_pantalla()

    if es_primer_tiempo:
        opcion3 = "Termino el primer tiempo"
    else:
        opcion3 = "Terminó el partido"
            
    tablero = f"""PRIMER TIEMPO
Equipo Local: {local} - {goles_local}
Equipo visitante: {visitante} - {goles_visitante}

1. Gol Local
2. Gol Visitante
3. {opcion3}
4. Salir
Ingrese una opción: """

    opcion = input(tablero)
    return opcion

def actualizar_goles(gol, local, visitante):
    if gol == "1":
        local += 1
    elif gol == "2":
        visitante += 1

    return local, visitante

def mostrar_resultados(opcion, local, visitante, goles_local, goles_visitante):
    limpiar_pantalla()

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

    opcion = mostrar_tablero(es_primer_tiempo, local, visitante, goles_local, goles_visitante)
    termino_partido = False
    while opcion != "4" and not termino_partido:
            goles_local, goles_visitante = actualizar_goles(opcion, goles_local, goles_visitante)
            opcion = mostrar_tablero(es_primer_tiempo, local, visitante, goles_local, goles_visitante)

            termino_partido = (not es_primer_tiempo) and opcion == "3"
            es_primer_tiempo = opcion != "3"

    return opcion, goles_local, goles_visitante

def principal():
    limpiar_pantalla()
    
    equipo_local = input("Ingrese el nombre del equipo local: ")
    equipo_visitante = input("Ingrese el nombre del equipo visitante: ")

    opcion, goles_local, goles_visitante = simular_partido(equipo_local, equipo_visitante)

    mostrar_resultados(opcion, equipo_local, equipo_visitante, goles_local, goles_visitante)

if __name__ == "__main__":
    principal()