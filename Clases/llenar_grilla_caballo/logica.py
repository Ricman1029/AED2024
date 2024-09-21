saltos = ((2, 1), (2, -1),
          (1, 2), (1, -2),
          (-2, 1), (-2, -1),
          (-1, 2), (-1, -2))


def generar_tablero(filas, columnas):
    tablero = []
    for i in range(filas):
        tablero.append([""] * columnas)

    return tablero


def actualizar_disponibilidad(tablero, posicion):
    disponibilidad = 0
    filas = len(tablero)
    columnas = len(tablero[0])
    for salto in saltos:
        fila_siguiente = posicion[0] + salto[0]
        columna_siguiente = posicion[1] + salto[1]
        if 0 <= fila_siguiente < filas and 0 <= columna_siguiente < columnas \
                and not tablero[fila_siguiente][columna_siguiente]:
            disponibilidad += 1
    return disponibilidad


def calcular_disponibilidades(tablero, posicion, disponibilidades):
    filas = len(tablero)
    columnas = len(tablero[0])
    for i in range(len(saltos)):
        fila_siguiente = posicion[0] + saltos[i][0]
        columna_siguiente = posicion[1] + saltos[i][1]
        if 0 <= fila_siguiente < filas and 0 <= columna_siguiente < columnas \
                and not tablero[fila_siguiente][columna_siguiente]:
            disponibilidades[i] = actualizar_disponibilidad(tablero, (fila_siguiente, columna_siguiente))


def buscar_indice_menor(lista):
    menor = None
    for i in range(len(lista)):
        if lista[i] is not None and (menor is None or lista[i] < lista[menor]):
            menor = i
    return menor


def saltar(tablero, posicion, salto, valor):
    fila = posicion[0] + saltos[salto][0]
    columna = posicion[1] + saltos[salto][1]
    tablero[fila][columna] = valor
    return [fila, columna]


def quedan_movimientos(tablero, posicion_actual):
    disponibilidad_saltos = [None] * 8
    calcular_disponibilidades(tablero, posicion_actual, disponibilidad_saltos)
    menor_diponibilidad = buscar_indice_menor(disponibilidad_saltos)
    if menor_diponibilidad is not None:
        return menor_diponibilidad
