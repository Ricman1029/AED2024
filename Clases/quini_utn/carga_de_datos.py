import glob
from dominio import QuiniUTN, Sorteo, Apuesta

def cargar_datos():
    with open("datos/sorteos.txt") as archivo:


    archivos = glob.glob("datos/apuestas*.txt")
    for ubicacion in archivos:
        with open(ubicacion) as archivo:




if __name__ == '__main__':
    cargar_datos()