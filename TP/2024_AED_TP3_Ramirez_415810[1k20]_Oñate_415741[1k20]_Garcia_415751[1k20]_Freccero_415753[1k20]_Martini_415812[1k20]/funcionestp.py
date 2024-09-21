from funciones import pais_destino, obtener_codigo_postal, obtener_direccion, obtener_forma_pago, obtener_tipo_envio
from entidades import Envio


def mostrar_cantidad_tipo(vector):
    for i in range (len(vector)):
        print (f"El envio de tipo {i} tiene {vector[i]} direcciones validas")
        
def mostrar_acumulado_envio(vector):
    for i in range (len(vector)):
        print(f"El acumulado del tipo de envío {i} es: {vector[i]}.")
        
def imprimir_datos (lista, cantidad): 
    for i in range (0, cantidad): 
        pais = pais_destino(lista[i].codigo_postal)
        print(lista[i], pais)

def cantidad_datos(lista):
    datos = int(input("Ingrese la cantidad de datos que desea ver. (0 para ver TODOS): "))
    if datos == 0:
        largo = len(lista)
        return largo
    else:
        return datos
                       
def opcion_borrar():
    opcion = input("¿Desea borrar todos los datos? Ingrese si o no: ")
    if opcion.lower() == "si":
        return True
    return False     

def leer_archivo(archivo, lista):
    linea = archivo.readline()
    while linea != "":
        codigo_postal = obtener_codigo_postal(linea)
        direccion = obtener_direccion(linea)
        tipo_envio = int(obtener_tipo_envio(linea))
        forma_pago = int(obtener_forma_pago(linea))
        envio = Envio(codigo_postal, direccion, tipo_envio, forma_pago)
        lista.append(envio)
        linea = archivo.readline()
        
def ingresar_tipo ():
    tipo = (input('Tipo de envio (0-6): '))
    while tipo not in ("0","1","2","3","4","5","6"):
        tipo = (input('Ingresar un número de tipo válido: '))
    return int(tipo) 

def ingresar_pago ():
    forma_pago = input('Forma de pago (1,2): ')
    while forma_pago not in ("1","2"):
        forma_pago = input('Ingrese un numero de pago válido: ')
    return int(forma_pago)

def selection_sort(lista):
    largo = len(lista)
    for i in range(largo-1):
        for j in range(i+1, largo):
            if lista[i].codigo_postal > lista[j].codigo_postal:
                lista[i], lista[j] = lista[j], lista[i]
