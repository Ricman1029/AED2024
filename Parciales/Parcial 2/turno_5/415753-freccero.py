def es_vocal(caracter)
    return caracter.upper() in "AEIOU"


def procesar_archivo(archivo):
    cadena = archivo.read()

    punto1 = 0
    punto2 = None
    punto3 = 0
    punto4 = 0

    cant_caracteres = 0

    # Punto 1
    hay_letra_pos_1 = hay_letra_pos_2 = hay_digito_impar = hay_digito = False

    # Punto 3
    cant_vocales = acum_pal_mas_vocales = total_palabras = 0

    for car in cadena:
        if car != " " and car != ".":
            """Estoy adentro de la palabra"""
            cant_caracteres += 1

            """Punto 1"""
            if cant_caracteres == 1:
                hay_letra_pos_1 = car.isalpha()
            elif cant_caracteres == 2:
                hay_letra_pos_2 = car.isalpha()
            elif car.isdigit():
                hay_digito = True
                if int(car) % 2 != 0:
                    hay_digito_impar = True

            """Punto 3"""
            if es_vocal(car):
                cant_vocales += 1

        else:
            """Terminé de leer la palabra"""
            """Punto 1"""
            if hay_letra_pos_1 and hay_letra_pos_2 and hay_digito and not hay_digito_impar:
                punto1 += 1

            """Punto 2"""
            if (punto2 is None or cant_caracteres < punto2) and cant_caracteres > 3:
                punto2 = cant_caracteres

            """Punto 3"""
            if 

            # Reseteamos las variables porque buscamos otra palabra
            cant_caracteres = 0
            hay_letra_pos_1 = hay_letra_pos_2 = hay_digito_impar = hay_digito = False

    return punto1, punto2, punto3, punto4


def principal():
    with open("entrada.txt") as archivo:
        r1, r2, r3, r4 = procesar_archivo(archivo)

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == "__main__":
    principal()