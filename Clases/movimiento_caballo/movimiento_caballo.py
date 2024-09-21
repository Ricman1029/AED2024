class Posicion:
    
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna

    def mover_punto(self, movimiento):
            return Posicion(self.fila + movimiento.fila, self.columna + movimiento.columna)

class Celda:
    def __init__(self, posicion, accesibilidad):
        self.orden = 0
        self.posicion = posicion
        self.accesibilidad = accesibilidad

    def disminuir_accesibilidad(self):
        self.accesibilidad -= 1
        
    def __str__(self):
        return str(self.orden)

class MovimientoCaballo:

    class MovimientosPosibles:
        MOVIMIENTOS_POSIBLES = [Posicion(fila, columna) for fila, columna 
                                in [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1),(-1, -2)]]
        
        def __init__(self, posicion, ancho, alto):
            self.actual = -1
            self.posicion = posicion
            self.ancho = ancho
            self.alto = alto

        def __iter__(self):
            return self
        
        def es_dentro_del_tablero(self, posicion, movimiento):
            nueva_posicion = posicion.mover_punto(movimiento)
            return 0 <= nueva_posicion.fila < self.alto and 0 <= nueva_posicion.columna < self.ancho

        def __next__(self):
            nueva_posicion = None 
            self.actual += 1     
            while self.actual < 8 and nueva_posicion is None:
                movimiento = self.MOVIMIENTOS_POSIBLES[self.actual]
                if self.es_dentro_del_tablero(self.posicion, movimiento):
                    nueva_posicion = self.posicion.mover_punto(movimiento)
                else:
                    self.actual += 1

            if self.actual == 8: 
                raise StopIteration
            
            return nueva_posicion

    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.tablero = self.crear_celdas(self.ancho, self.alto) 
        self.celda_actual = self.tablero[0][0]
        self.celda_actual.orden = 1
        
    def movimientos_posibles(self, posicion):
        return MovimientoCaballo.MovimientosPosibles(posicion, self.ancho, self.alto)
    
    def obtener_celda(self, posicion):
        return self.tablero[posicion.fila][posicion.columna]
    
    def crear_celda(self, i, j):
        posicion = Posicion(i, j)
        return Celda(posicion, self.calcular_accesibilidad(posicion))
        
    def crear_celdas(self, ancho, alto):        
        return [[self.crear_celda(i, j) for j in range(ancho)] for i in range(alto)]

    def calcular_accesibilidad(self, posicion):
        return len([1 for _ in self.movimientos_posibles(posicion)])
    
    def actualizar_accesibilidad_alrededor(self, celda):
        for nueva_posicion in self.movimientos_posibles(celda.posicion):
            self.obtener_celda(nueva_posicion).disminuir_accesibilidad()

    def mover_a(self, celda):
        celda.orden = self.celda_actual.orden + 1 
        self.actualizar_accesibilidad_alrededor(celda)
        self.celda_actual = celda

    def siguiente_celda(self):
        celda_menor_accesibilidad = None
        for nueva_posicion in self.movimientos_posibles(self.celda_actual.posicion):
            celda = self.obtener_celda(nueva_posicion)
            if celda.orden == 0:
                if celda_menor_accesibilidad is None or celda.accesibilidad < celda_menor_accesibilidad.accesibilidad: 
                    celda_menor_accesibilidad = celda
        return celda_menor_accesibilidad

    def mover_siguiente(self):
        siguiente = self.siguiente_celda()
        if siguiente is not None:
            self.mover_a(siguiente)
        return siguiente

