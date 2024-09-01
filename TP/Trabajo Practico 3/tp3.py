
from entidades import Envio

def menu():
    print("1. Limpiar y cargar envíos")
    print("2. Cargar por teclado el envío")
    print("3. Mostrar envíos")
    print("4. Buscar dirección y tipo de envío")
    print("5. Buscar por código postal")
    print("6. Cantidad de envíos (HC o SC)")
    print("7. Importe final acumulado por tipo de envío")
    print("8. Mayor importe final por tipo de envío")
    print("9. Promedio y envíos menores al promedio")

def ejecutar_opcion(opcion):
    if opcion == "1":
        limpiar_cargar_envios()
    elif opcion == "2":
        cargar_teclado_envio()
    elif opcion == "3":
        mostrar_envios()
    elif opcion == "4":
        buscar_direccion_tipo()
    elif opcion == "5":
        buscar_por_codigo_postal()
    elif opcion == "6":
        cantidad_de_envios_HC_SC()
    elif opcion == "7":
        importe_final_acumulado()
    elif opcion == "8":
        mayor_importe_final()
    elif opcion == "9":
        promedio_envios_menores()

def limpiar_cargar_envios():
    print("Limpiar y cargar envíos")

def cargar_teclado_envio(lista):
    print("Cargar por teclado el envío")
    
    codigo_postal = input('Codigo postal: ')
    direccion = input('Direccion: ')
    tipo = input('Tipo de envio (0-6): ')
    forma_pago = input('Forma de pago (1,2): ')
    print()
    lista.append (Envio (codigo_postal, direccion, tipo, forma_pago))

def mostrar_envios():
    print("Mostrar envíos")

def buscar_direccion_tipo():
    print("Buscar dirección y tipo de envío")

def buscar_por_codigo_postal():
    print("Buscar por código postal")

def cantidad_de_envios_HC_SC():
    print("Cantidad de envíos (HC o SC)")

def importe_final_acumulado():
    print("Importe final acumulado por tipo de envío")

def mayor_importe_final():
    print("Mayor importe final por tipo de envío")

def promedio_envios_menores():
    print("Promedio y envíos menores al promedio")

def principal ():
    lista_envios = ["hola"]
    print(lista_envios)
    cargar_teclado_envio (lista_envios)
    print(lista_envios[1])
    menu()
    opcion = input("Seleccione una opción: ")
    return opcion


if __name__ == "__main__":
    principal()