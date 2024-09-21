from logica import generar_tablero, llenar_tablero
from consola import mostrar_tablero


class Contexto:
    def __init__(self, posicion_actual, movimiento):
        self.posicion_actual = posicion_actual
        self.movimiento = movimiento
        self.convertir_posicion_actual()

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
    filas = int(input("Filas: "))
    columnas = int(input("Columnas: "))
    tablero = generar_tablero(filas, columnas)

    posicion_actual = input("Indique la posición en la que desea empezar ('fila,columna'): ")
    contexto = Contexto(posicion_actual, 1)
    tablero[contexto.devolver_posicion_actual_en(0)][contexto.devolver_posicion_actual_en(1)] = contexto.movimiento
    mostrar_tablero(tablero)

    while llenar_tablero(tablero, contexto) is not None:
        mostrar_tablero(tablero)


if __name__ == '__main__':
    principal()