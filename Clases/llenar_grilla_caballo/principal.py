from logica import generar_tablero, quedan_movimientos, saltar
from consola import mostrar_tablero, preguntar_modo


class Contexto:
    def __init__(self, posicion_actual, movimiento):
        self.posicion_actual = posicion_actual
        self.movimiento = movimiento
        self.convertir_posicion_actual()
        self.salto = None

    def convertir_posicion_actual(self):
        lista = self.posicion_actual.split(",")
        for i in range(len(lista)):
            lista[i] = int(lista[i])
        self.posicion_actual = lista

    def devolver_posicion_actual(self):
        return self.posicion_actual

    def devolver_posicion_actual_en(self, indice):
        return self.posicion_actual[indice]


def principal():
    modo_visualizacion = preguntar_modo()

    filas = int(input("Filas: "))
    columnas = int(input("Columnas: "))
    tablero = generar_tablero(filas, columnas)

    posicion_actual = input("Indique la posición en la que desea empezar ('fila,columna'): ")
    contexto = Contexto(posicion_actual, 1)
    tablero[contexto.devolver_posicion_actual_en(0)][contexto.devolver_posicion_actual_en(1)] = contexto.movimiento
    mostrar_tablero(tablero, contexto.movimiento)

    contexto.salto = quedan_movimientos(tablero, contexto.posicion_actual)
    while contexto.salto is not None:
        contexto.movimiento += 1
        contexto.posicion_actual = saltar(tablero, contexto.posicion_actual, contexto.salto, contexto.movimiento)
        mostrar_tablero(tablero, contexto.movimiento)
        if modo_visualizacion == "Manual":
            input("Presione una tecla para continuar")
        contexto.salto = quedan_movimientos(tablero, contexto.posicion_actual)


if __name__ == '__main__':
    principal()