class Equipo:
    def __init__(self, nombre, puntos, goles):
        self.nombre = nombre
        self.puntos = puntos
        self.goles = goles

    def __str__(self):
        return f"Equipo: {self.nombre} - Puntos: {self.puntos} - Goles: {self.goles}"