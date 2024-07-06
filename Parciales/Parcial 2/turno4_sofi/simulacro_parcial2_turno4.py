def leer_cadena():
    with open("entraditas.txt", "r") as archivo:
        cadena = archivo.read()
    return cadena


def mostrar_resultados(r1):
    print("Primer resultado:", r1)
    # print("Segundo resultado:", r2)
    # print("Tercer resultado:", r3)
    # print("Cuarto resultado:", r4)


def busco_mayuscula(caracter):
    if caracter.isupper():
        return True
    return False


def busco_digito_2_4(palabra, senal_mayuscula, contador):
    if palabra[1].isdigit() and palabra[3].isdigit() and senal_mayuscula is False:
        contador += 1
    return contador


def principal():
    cadena = leer_cadena()
    contador_r1 = 0
    senal_mayuscula = None
    palabra = ''

    for car in cadena:
        if car == ' ' or car == '.':
            # Termino una palabra
            r1 = busco_digito_2_4(palabra, senal_mayuscula, contador_r1)

            palabra = ''
            senal_mayuscula = False

        else:
            senal_mayuscula = busco_mayuscula(car)

            # Dentro de la palabra
            palabra += car

    mostrar_resultados(r1)


if __name__ == "_main_":
    principal()

