import random

ROJO = "\033[91m"
VERDE = "\033[92m"
RESET = "\033[0m"
AMARILLO = "\033[93m"


def hacer_bolillero():
    return list(random.choice([True, False]) for _ in range(0, 90))


def fila_bolillero(bolillero, i, j):
    numero = i*10 + j
    print_amarillo('║')
    if bolillero[numero]:
        # Salio
        print_rojo(f'{numero:02}')
    else:
        # No salio
        print_verde(f'{numero:02}')

def print_amarillo(texto): 
    print(f"{AMARILLO}{texto}{RESET}", end='')

def print_rojo(texto): 
    print(f"{ROJO}{texto}{RESET}", end='')

def print_verde(texto): 
    print(f"{VERDE}{texto}{RESET}", end='')


def dibujar_bolillero(bolillero: list):
    print_amarillo('╔══╦══╦══╦══╦══╦══╦══╦══╦══╦══╗')   
    print() 

    # For filas
    for i in range(9):
        # For columnas
        for j in range(10):
            fila_bolillero(bolillero, i, j)
        print_amarillo('║')
        print()

        if i < 8:
            print_amarillo('╠══╬══╬══╬══╬══╬══╬══╬══╬══╬══╣')
            print()        
    print_amarillo('╚══╩══╩══╩══╩══╩══╩══╩══╩══╩══╝')
    print()

if (__name__ == "__main__"):
    # test
    bolillero = hacer_bolillero()

    dibujar_bolillero(bolillero)
