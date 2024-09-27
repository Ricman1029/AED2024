class Posicion:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Celda:
    def __init__(self, posicion: Posicion, posiciones_asociadas):
        self.posicion = posicion
        self.posiciones_de_celdas_asociadas = posiciones_asociadas
        self.disponibilidad = len(self.posiciones_de_celdas_asociadas)
        self.valor = ""

    def disminuir_disponibilidad(self):
        self.disponibilidad -= 1



class Tablero:
    SALTOS = ((2, 1), (2, -1), (1, 2), (1, -2), (-2, 1), (-2, -1), (-1, 2), (-1, -2))

    def __init__(self, filas, columnas, posicion_inicial):
        self.filas = filas
        self.columnas = columnas
        self.tablero = self.crear_tablero(self.filas, self.columnas)
        self.posicion_actual = self.obtener_posicion_inicial(posicion_inicial)
        self.movimiento = 0
        self.saltar()

    def crear_tablero(self, filas, columnas):
        tablero = []
        for i in range(filas):
            tablero.append([0] * columnas)
            for j in range(columnas):
                posiciones_asociadas = self.obtener_posiciones_asociadas_a_celda(Posicion(i, j))
                tablero[i][j] = Celda(Posicion(j, i), posiciones_asociadas)
        return tablero

    def obtener_posiciones_asociadas_a_celda(self, posicion: Posicion):
        posiciones_asociadas = []
        for salto in self.SALTOS:
            posicion_asociada = Posicion(posicion.x + salto[0], posicion.y + salto[1])
            if 0 <= posicion_asociada.x < self.filas and 0 <= posicion_asociada.y < self.columnas:
                posiciones_asociadas.append(posicion_asociada)
        return posiciones_asociadas

    def obtener_posicion_inicial(self, posicion_incial):
        coordenadas = self.obtener_coordenadas(posicion_incial)
        return Posicion(coordenadas[0], coordenadas[1])

    def obtener_coordenadas(self, posicion_incial):
        coordenadas = posicion_incial.split(",")
        coordenadas[0] = int(coordenadas[0])
        coordenadas[1] = int(coordenadas[1])
        return coordenadas

    def obtener_celda(self, posicion: Posicion):
        return self.tablero[posicion.x][posicion.y]

    def siguiente_salto(self):
        menor = nueva_posicion = None
        celda = self.obtener_celda(self.posicion_actual)
        for posicion in celda.posiciones_de_celdas_asociadas:
            siguiente_celda = self.obtener_celda(posicion)
            if siguiente_celda.disponibilidad >= 0 and (menor is None or menor > siguiente_celda.disponibilidad):
                menor, nueva_posicion = siguiente_celda.disponibilidad, posicion

        self.posicion_actual = nueva_posicion
        return nueva_posicion

    def saltar(self):
        self.movimiento += 1
        celda = self.tablero[self.posicion_actual.x][self.posicion_actual.y]
        celda.valor = self.movimiento
        celda.disponibilidad = 0
        self.actualizar_disponibilidad_celdas_asociadas(celda)

    def actualizar_disponibilidad_celdas_asociadas(self, celda: Celda):
        for posicion in celda.posiciones_de_celdas_asociadas:
            self.tablero[posicion.x][posicion.y].disminuir_disponibilidad()
