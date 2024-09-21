class Ticket:
    def __init__(self, codigo_vuelo, id_pasajero, pais_destino, numero_asiento, importe):
        self.codigo_vuelo = codigo_vuelo
        self.id_pasajero = id_pasajero
        self.pais_destino = pais_destino
        self.numero_asiento = numero_asiento
        self.importe = importe
        
    def __str__(self):
        return f"Código vuelo: {self.codigo_vuelo} - Id Pasajero: {self.id_pasajero} - " + \
               f"Id destino: {self.pais_destino} - " + \
               f"Número asiento: {self.numero_asiento} - Importe: ${self.importe}"