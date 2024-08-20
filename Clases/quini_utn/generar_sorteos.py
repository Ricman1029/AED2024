import random
import datetime


def generar_archivo_apuesta(fecha, numeros_posibles, ids):
    apuestas = ((ids.pop(), *random.sample(numeros_posibles, 6)) for i in range(0, 10000))
            
    archivo_sorteo =  open(f'apuestas_{fecha}.txt', 'w') 
    for apuesta in apuestas:
        linea_apuesta = f"{apuesta}".replace("(","").replace(")", "").replace("'", "").replace(" ", "")
        archivo_sorteo.write(linea_apuesta+ "\n")

    archivo_sorteo.close()

def generar_sorteos_y_apuestas():
    fecha = datetime.date(2024, 1, 1)
    fecha_formato = lambda fecha: f"{fecha.year}{fecha.month:02}{fecha.day:02}"
    fecha_sumar_dia = lambda fecha, dias: fecha + datetime.timedelta(days = dias)
    numeros_posibles = list(range(0, 46)) #0 - 45

    ids_apuestas = list(range(0,1000000))
    random.shuffle(ids_apuestas)

    sorteos = list(
            (fecha_formato(fecha_sumar_dia(fecha, i)), 
             *random.sample(numeros_posibles, k=6))  
            for i in range(1, 10)
        )

    archivo_sorteo =  open('datos/sorteos.txt', 'w')
    for sorteo in sorteos:
        linea_sorteo = f"{sorteo}"
        linea_sorteo = linea_sorteo.replace("'","").replace("(", "").replace(")", "").replace(" ", "")
        archivo_sorteo.write(linea_sorteo + "\n")

        generar_archivo_apuesta(sorteo[0], numeros_posibles, ids_apuestas) # fecha con formato
        
    archivo_sorteo.close()

generar_sorteos_y_apuestas()