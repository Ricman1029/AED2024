# Imprimir los primeros 100 numeros de fibonacci (de 3 numeros) empezando desde el 2021, 2022, 2023
def principal():
    primero = 2021
    segundo = 2022
    tercero = 2023

    for i in range(100):
        print(primero)
        primero, segundo, tercero = segundo, tercero, primero + segundo + tercero


if __name__ == '__main__':
    principal()