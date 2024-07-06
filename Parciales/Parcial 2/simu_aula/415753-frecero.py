def es_vocal(car):
    return car.upper() in "AEIOU"


def calcular_promedio(acumulador, contador):
    if contador != 0:
        return int(acumulador / contador)
    return 0


def procesar_archivo(cadena):
    punto1 = punto3 = punto4 = 0
    punto2 = None

    # Punto 1
    cant_caracteres = cant_vocales = cant_consonantes = 0

    # Punto 2
    tiene_digito = tiene_p = False

    # Punto 3
    tiene_s = False
    acumulador_punto3 = contador_punto3 = 0

    # Punto 4
    tiene_r = tiene_ra = tiene_vocal_pos_1_2 = False

    for car in cadena:
        if car != " " and car != ".":
            """Estoy en la palabra"""
            """Punto 1"""
            cant_caracteres += 1
            if es_vocal(car):
                cant_vocales += 1
            elif car.isalpha() and not es_vocal(car):
                cant_consonantes += 1

            """Punto 2"""
            if car.isdigit():
                tiene_digito = True
            elif car.upper() == "P":
                tiene_p = True

            """Punto 3"""
            if car.upper() == "S":
                tiene_s = True

            """Punto 4"""
            if cant_caracteres <= 2 and es_vocal(car):
                tiene_vocal_pos_1_2 = True

            if tiene_r and car.upper() == "A":
                tiene_ra = True
            tiene_r = car.upper() == "R"

        else:
            """Terminé de leer la palabra"""
            """Punto 1"""
            if cant_caracteres % 2 == 0 and cant_vocales == cant_consonantes:
                punto1 += 1

            """Punto 2"""
            if tiene_digito and not tiene_p:
                if punto2 is None or cant_caracteres > punto2:
                    punto2 = cant_caracteres

            """Punto 3"""
            if cant_caracteres > 2 and tiene_s:
                acumulador_punto3 += cant_caracteres
                contador_punto3 += 1

            """Punto 4"""
            if tiene_ra and tiene_vocal_pos_1_2:
                punto4 += 1

            # Reseteo las variables porque empieza otra palabra
            cant_caracteres = cant_vocales = cant_consonantes = 0
            tiene_digito = tiene_p = False
            tiene_s = False
            tiene_r = tiene_ra = tiene_vocal_pos_1_2 = False

    punto3 = calcular_promedio(acumulador_punto3, contador_punto3)

    return punto1, punto2, punto3, punto4


def principal():
    with open("entrada.txt") as archivo:
        cadena = archivo.read()
        r1, r2, r3, r4 = procesar_archivo(cadena)

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == "__main__":
    principal()
