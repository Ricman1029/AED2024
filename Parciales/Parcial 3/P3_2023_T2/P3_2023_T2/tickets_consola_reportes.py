def mostrar_ticket(id_pasajero, ticket):
    if ticket is not None:
        print(ticket)
    else:
        print(f"No se encontró el ticket para el id pasajero {id_pasajero}")


def mostrar_tickets(tickets):
    for i, ticket in enumerate(tickets):
        print(f"{i}, {ticket}")    
        
def mostrar_importes_por_pais(importes_por_pais, importe_inferior):
    for i, importe in enumerate(importes_por_pais):
        if importe > importe_inferior:
            print(f"{i + 1}. {importe}")



