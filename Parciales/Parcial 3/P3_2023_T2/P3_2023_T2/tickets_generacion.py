import random
import string
from tickets_entidades import Ticket

def generar_vuelos(n):
    vuelos = []
    for i in range(0, n):
        codigo_vuelo = ""
        for i in range(0, 4): #4 letras
            codigo_vuelo += random.choice(string.ascii_uppercase)
        codigo_vuelo += str(random.randint(100, 1000)) #3 dígito
        vuelos.append((codigo_vuelo, list(range(1, 301)))) # código de vuelo y asientos disponibles. 
                                                        #Una solución para que no se repitan los asientos
    return vuelos
        

def generar_tickets(tickets, n):
    vuelos = generar_vuelos(20)
    for i in range(n):
        vuelo = random.choice(vuelos)
        codigo_vuelo = vuelo[0] #Código de vuelo 
        pais_destino = random.randint(1, 20)
        id_pasajero = random.randint(10000, 100000 * n)
        nro_asiento = random.choice(vuelo[1]) #qué pasa cuando se acaban lo asientos?
        vuelo[1].remove(nro_asiento)
        importe = round(random.uniform(300000, 10000000), 2)
        tickets.append(Ticket(codigo_vuelo, id_pasajero, pais_destino, nro_asiento, importe))

if __name__ == "__main__":
    tickets = []
    generar_tickets(tickets, 5000)
    for ticket in tickets:
        print(ticket)