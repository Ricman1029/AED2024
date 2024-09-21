def obtener_importes_por_pais(tickets):
    importes = [0] * 20
    for ticket in tickets:
        if 1 <= ticket.pais_destino <=20:
            importes[ticket.pais_destino - 1] += ticket.importe
    return importes

def obtener_tickets_con_asientos_mayores_a(tickets, nro_asiento):
    tickets_con_asientos_mayores_a = []
    for ticket in tickets:
        if ticket.numero_asiento > nro_asiento:
            tickets_con_asientos_mayores_a.append(ticket)
    return tickets_con_asientos_mayores_a
    
def ordenar_por_codigo_vuelo(tickets):
    long = len(tickets)
    for i in range(long):
        ordenado = True
        for j in range(long - i - 1):
            if tickets[j].codigo_vuelo > tickets[j + 1].codigo_vuelo:
                tickets[j], tickets[j + 1] = tickets[j + 1], tickets[j]    
                ordenado = False
        if ordenado:
            return

def buscar_ticket_por_id_pasajero(tickets, id_pasajero):
    for ticket in tickets:
        if ticket.id_pasajero == id_pasajero:
            return ticket
    return None

