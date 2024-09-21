from entidades import Envio
from funciones import pais_destino, determinar_importe_final, seleccion, mostrar_cantidad_tipo, mostrar_acumulado_envio, cantidad_datos, opcion_borrar, leer_archivo, limpiar_cargar_envios, ingresar_tipo, ingresar_pago, imprimir_datos, buscar_direccion_tipo, mostrar_direccion_tipo, modificar_forma_pago, determinar_control, validacion_envios, obtener_codigo_postal, obtener_direccion,obtener_forma_pago, obtener_tipo_envio, funcion_codigo_postal

class Context:
    def __init__(self):
        self.tipo_control = "Hard Control"
        self.envios = []
        self.importes_por_tipo = [0] * 7
           
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
    print("10. Salir")
    
def ejecutar_opcion(opcion, contexto):
    if opcion == "1":
        limpiar_cargar_envios(contexto.envios, contexto.tipo_control)
    elif opcion == "2":
        cargar_teclado_envio(contexto.envios)
    elif opcion == "3":
        mostrar_envios(contexto.envios)
    elif opcion == "4":
        mostrar_direccion_tipo(contexto.envios)
    elif opcion == "5":
        modificar_forma_pago(contexto.envios)
    elif opcion == "6":
        cantidad_de_envios_HC_SC(contexto.envios, contexto.tipo_control)
    elif opcion == "7":
        importe_final_acumulado(contexto.envios, contexto.tipo_control, contexto.importes_por_tipo)
    elif opcion == "8":
        mayor_importe_final(contexto.importes_por_tipo)
    elif opcion == "9":
        promedio_envios_menores(contexto.envios)
    elif opcion == "10":
        salir()
        
def limpiar_cargar_envios(envios, control):
    print("Limpiar y cargar envíos")
    opcion = opcion_borrar()
    if opcion == True:
        envios.clear()
        with open ("envios-tp3.txt" , "r") as archivo:
          linea = archivo.readline()
          control = determinar_control(linea)
          leer_archivo(archivo, envios)
          
def cargar_teclado_envio(envios):
    print("Cargar por teclado el envío")
    codigo_postal = input('Codigo postal: ')
    direccion = input('Direccion: ')
    tipo = ingresar_tipo()
    forma_pago = ingresar_pago()
    print()
    envios.append (Envio (codigo_postal, direccion, tipo, forma_pago))
    
def mostrar_envios(envios): #punto 3
    print("Mostrar envíos")
    seleccion(envios)
    primeros_numeros = cantidad_datos(envios)
    imprimir_datos(envios, primeros_numeros)

def buscar_por_codigo_postal(envios, codigo_postal):
    print("Buscar por código postal")
    indice = 0
    while indice < len(envios) and codigo_postal != envios[indice].codigo_postal:
        indice += 1
    if indice < (len(envios)):
        return indice
    return None

def mostrar_direccion_tipo(envios):
    print("Buscar dirección y tipo de envío")
    direccion = input("Ingresa la dirección: ")
    tipo_envio = int(input("Ingresa el tipo de envio: "))
    indice = buscar_direccion_tipo(direccion, tipo_envio, envios)
    if indice is not None:
        print(envios[indice])
    else:
        print ("No se encontro ninguna coincidencia.") 

def modificar_forma_pago(envios):
    codigo_postal = input("Ingresa un codigo postal: ")
    indice = buscar_por_codigo_postal(envios, codigo_postal)
    if indice is not None:  # Si encontró coincidencias
        if envios[indice].forma_pago == 1:
            envios[indice].forma_pago = 2
        else:
            envios[indice].forma_pago = 1
        print(envios[indice])  # Muestra el objeto modificado
    else:
        print("No se encontró ninguna coincidencia.")    

def cantidad_de_envios_HC_SC(envios, control):
    print("Cantidad de envíos (HC o SC)")
    contadores_por_tipo_envio = [0,0,0,0,0,0,0]

    for i in range (len(envios)):
        if control == "Soft Control" or validacion_envios(envios[i].direccion):
            contadores_por_tipo_envio[envios[i].tipo] += 1

    mostrar_cantidad_tipo(contadores_por_tipo_envio)

def importe_final_acumulado(envios, control, acumuladores_por_tipo_envio):
    print("Importe final acumulado por tipo de envío")

    for i in range (len(envios)):
        if control == "Soft Control" or validacion_envios(envios[i].direccion):
            destino = pais_destino(envios[i].codigo_postal)
            importe_final = determinar_importe_final(envios[i].codigo_postal, destino, envios[i].tipo, envios[i].forma_pago)
            acumuladores_por_tipo_envio[envios[i].tipo] += importe_final

    mostrar_acumulado_envio(acumuladores_por_tipo_envio)

def mayor_importe_final(acumuladores_por_tipo_envio):
    print("Mayor importe final por tipo de envío")
    mayor = total = 0
    if acumuladores_por_tipo_envio == None:
        print("Error")
        return    
    
    for i in range (len(acumuladores_por_tipo_envio)):
        if acumuladores_por_tipo_envio[i] > mayor:
            mayor = acumuladores_por_tipo_envio[i]
            posicion = i   
        total += acumuladores_por_tipo_envio[i]

    if total != 0:
        porcentaje = mayor * 100 // total
    else:
        print("Los importes finales acumulados por tipo de envío todavía no fueron calculados.")
        return
    
    print (f"El mayor importe acumulado es: {mayor} y el tipo de envío es {posicion}")
    print (f"El porcentaje entero que representa el mayor importe es: {porcentaje}%")

def promedio_envios_menores(envios):
    print("Promedio y envíos menores al promedio")
    
    acumulador = contador_menores = 0
    
    for i in range (len(envios)):
        destino = pais_destino(envios[i].codigo_postal)
        final = determinar_importe_final(envios[i].codigo_postal, destino, envios[i].tipo, envios[i].forma_pago)
        acumulador += final
    
    promedio = acumulador // len(envios)
    
    for i in range (len(envios)):
        destino = pais_destino(envios[i].codigo_postal)
        final = determinar_importe_final(envios[i].codigo_postal, destino, envios[i].tipo, envios[i].forma_pago)
        if final < promedio:
            contador_menores += 1  
       
    print (f"El importe final promedio es: {promedio}")
    print (f"Cantidad de envíos con importe menor al promedio: {contador_menores}")

def salir():
    print("Salir")

def principal ():
    menu()
    contexto = Context()
    opcion = input("Seleccione una opción: ")
    while opcion != "10":
        ejecutar_opcion(opcion, contexto)
        menu() # siempre que elijo una opcion, se ejecuta el menu de opciones de nuevo
        opcion = input("Seleccione una opción: ")
    
if __name__ == "__main__":
    principal()