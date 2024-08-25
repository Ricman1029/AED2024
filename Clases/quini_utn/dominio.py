class Sorteo:
    def __init__(self, fecha, numeros):
        self.fecha = fecha
        self.numeros = numeros


class Apuesta:
    def __init__(self, id, numeros):
        self.id = id
        self.numeros = numeros


class ApuestasDia:
    def __init__(self, fecha, apuestas):
        self.fecha = fecha
        self.apuestas = apuestas


class QuiniUTN:
    def __init__(self, sorteos, historial_apuestas):
        self.sorteos = sorteos
        self.historial_apuestas = historial_apuestas


