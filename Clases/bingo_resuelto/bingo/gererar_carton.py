import random

def borrar_numeros(carton, fila):
    for i in range(4):
        indice = random.randint(0, 8)
        carton[fila][indice] = None


def agregar_numeros(carton, min, max, fila):

    for columna in range(9):
        numero = random.randint(columna * 10 + min, columna * 10 + max)
        carton[fila][columna] = (numero, False)

def generar_carton():
    filas = 3
    columnas = 9
    carton = []

    for i in range(filas):
        fila = [()] * columnas  # Crea una fila con columnas tuplas vacías
        carton.append(fila)  # Añade la fila a la matriz

    # Llamamos a agregar numero
    agregar_numeros(carton, 0, 3, 0)
    agregar_numeros(carton, 4, 6, 1)
    agregar_numeros(carton, 7, 9, 2)

    for i in range(3):
        borrar_numeros(carton, i)

    return carton


def dibujar_carton(carton):
    # Imprimir la matriz para visualizarla
    for fila in carton:
        print(fila)


if __name__ == "__main__":
    # Llamar a la función para dibujar la matriz
    carton = generar_carton()
    dibujar_carton(carton)
