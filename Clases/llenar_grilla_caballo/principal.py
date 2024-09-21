from logica import generar_tablero, calcular_salto, saltar, convertir_en_lista
from consola import mostrar_tablero, preguntar_modo


def principal():
    modo_visualizacion = preguntar_modo()

    filas = int(input("Filas: "))
    columnas = int(input("Columnas: "))
    tablero = generar_tablero(filas, columnas)

    posicion_inicial = input("Indique la posición en la que desea empezar ('fila,columna'): ")
    posicion_actual = convertir_en_lista(posicion_inicial)
    movimiento = 1
    tablero[posicion_actual[0]][posicion_actual[1]] = movimiento
    mostrar_tablero(tablero, movimiento)

    salto = calcular_salto(tablero, posicion_actual)
    while salto is not None:
        movimiento += 1
        posicion_actual = saltar(tablero, posicion_actual, salto, movimiento)
        mostrar_tablero(tablero, movimiento)

        if modo_visualizacion == "Manual":
            input("Presione una tecla para continuar")
        salto = calcular_salto(tablero, posicion_actual)


if __name__ == '__main__':
    principal()