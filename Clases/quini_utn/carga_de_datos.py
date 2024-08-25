import glob
from dominio import QuiniUTN, Sorteo, Apuesta, ApuestasDia
from funciones_de_listas import partir_cadena, orden_parcial, buscar_indice


def crear_historico_apuestas():
    historico_apuestas = []

    ubicaciones = glob.glob("datos/apuestas_*.txt")
    for ubicacion in ubicaciones:
        apuestas = []
        with open(ubicacion) as archivo:
            indice_fecha = buscar_indice("_", ubicacion) + 1
            fecha = ubicacion[indice_fecha:indice_fecha + 8]
            linea = archivo.readline()
            while linea != "":
                lista = partir_cadena(linea, ",\n", int)
                apuesta = Apuesta(lista[0], lista[1:])
                apuestas.append(apuesta)
                linea = archivo.readline()
            apuestas_dia = ApuestasDia(fecha, apuestas)
            historico_apuestas.append(apuestas_dia)

    return historico_apuestas


def crear_lista_sorteos():
    sorteos = []
    with open("datos/sorteos.txt") as archivo:
        linea = archivo.readline()
        while linea != "":
            lista = partir_cadena(linea, ",\n", int)
            lista = orden_parcial(lista, 1, len(lista))
            sorteo = Sorteo(lista[0], lista[1:])
            sorteos.append(sorteo)
            linea = archivo.readline()

    return sorteos


def cargar_datos():
    sorteos = crear_lista_sorteos()
    historico_apuestas = crear_historico_apuestas()

    quini_utn = QuiniUTN(sorteos, historico_apuestas)

    return quini_utn


if __name__ == '__main__':
    cargar_datos()
