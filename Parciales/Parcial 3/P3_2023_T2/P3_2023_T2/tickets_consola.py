import os
from tickets_generacion import generar_tickets
from tickets_negocio import obtener_importes_por_pais, obtener_tickets_con_asientos_mayores_a, ordenar_por_codigo_vuelo, buscar_ticket_por_id_pasajero
from tickets_consola_reportes import mostrar_importes_por_pais, mostrar_tickets, mostrar_ticket


def limpiar_pantalla():
    os.system("cls")
    
def ingresar_numero(texto):
    while not (n := input(texto)).isdigit():
        pass
    return int(n)
    
# Punto 1
def ejecutar_cargar_tickets(tickets):
    n = ingresar_numero("Ingresar la cantidad de tickets a generar: ")
    tickets.clear()
    generar_tickets(tickets, n)
    print(f"Se crearon {len(tickets)} tickets")


# Punto 2
def ejecutar_mostrar_tickets_asientos_mayores_a(tickets):
    numero_asiento = int(input("Número de asiento: "))
    
    tickets_con_asientos_mayores_a = obtener_tickets_con_asientos_mayores_a(tickets, numero_asiento)
    print(f"Se recuperaron {len(tickets_con_asientos_mayores_a)} tickets con asientos mayores a {numero_asiento}")
    ordenar_por_codigo_vuelo(tickets_con_asientos_mayores_a)
    mostrar_tickets(tickets_con_asientos_mayores_a)

# Punto 3    
def ejecutar_mostrar_importes_por_pais(empleos):
    importes_por_pais = obtener_importes_por_pais(empleos)
    print("Se muestran los importes acumulados por país mayores al importe ingresado.")
    importe = float(input("Importe: "))
    mostrar_importes_por_pais(importes_por_pais, importe)
    
# Punto 4  
def ejecutar_mostrar_ticket_por_pasajero(tickets):
    identificador = ingresar_numero("Ingresar identificador de pasajero: ")
    ticket = buscar_ticket_por_id_pasajero(tickets, identificador)
    mostrar_ticket(identificador, ticket)

# region Menú principal y ejecución de opciones
def ejecutar_opcion(opcion, tickets):
    if opcion == "a":
        ejecutar_cargar_tickets(tickets)
    else:
        if len(tickets) == 0:
            print("Primero debe ejecutar la opción a para cargar los tickets")
        else: 
            if opcion == "b":
                ejecutar_mostrar_tickets_asientos_mayores_a(tickets)
            elif opcion == "c":
                ejecutar_mostrar_importes_por_pais(tickets)
            else:
                ejecutar_mostrar_ticket_por_pasajero(tickets)            

def parar_seguir():
    input("Presione ENTER para continuar")

def mostrar_menu():
    menu = '''a. Cargar tickets
b. Tickets con asientos mayores a N
c. Importes por país
d. Ticket por pasajero
s. Salir'''
    print(menu)

def ingresar_opcion():
    opcion = input("Opción: ")
    while opcion not in ("a", "b", "c", "d", "s"):
        opcion = input("Opción: ")
    return opcion

def elegir_opcion_menu():
    limpiar_pantalla()
    mostrar_menu()
    return ingresar_opcion()

def principal():
    tickets = []
    while (opcion := elegir_opcion_menu()) != "s":
        limpiar_pantalla()
        ejecutar_opcion(opcion, tickets)
        parar_seguir()
# endregion

if __name__ == "__main__":
    principal()