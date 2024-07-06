def es_vocal(car):
    return car.upper() in "AEIOU"


def calcular_promedio(acumulador, contador):
    if contador != 0:
        return int(acumulador / contador)
    return 0


def procesar_texto(archivo):
    cadena = archivo.read()

    punto1 = 0
    punto2 = None
    punto3 = punto4 = 0

    # Punto 1
    cant_letras = cant_consonantes = 0

    # Punto 2
    vocal_en_pos_2 = tiene_n = False

    # Punto 3
    tiene_g_en_pos_2 = tiene_digito = False
    acumulador_punto3 = contador_punto3 = 0

    # Punto 4
    empieza_con_vocal = tiene_pe = tiene_p = False

    for car in cadena:
        if car != " " and car != ".":
            """Estamos adentro de la palabra"""
            """Punto 1"""
            cant_letras += 1
            if car.isalpha() and not es_vocal(car):
                cant_consonantes += 1

            """Punto 2"""
            if cant_letras == 2 and es_vocal(car):
                vocal_en_pos_2 = True
            if car.upper() == "N":
                tiene_n = True

            """Punto 3"""
            if cant_letras == 2 and car.upper() == "G":
                tiene_g_en_pos_2 = True
            if car.isdigit():
                tiene_digito = True

            """Punto 4"""
            if es_vocal(car) and cant_letras == 1:
                empieza_con_vocal = True

            if not empieza_con_vocal:
                if tiene_p and car.upper() == "E":
                    tiene_pe = True
                tiene_p = car.upper() == "P"

        else:
            """Terminamos de leer la palabra"""
            """Punto 1"""
            if cant_letras % 2 != 0 and cant_consonantes == 1:
                punto1 += 1

            """Punto 2"""
            if vocal_en_pos_2 and not tiene_n:
                if punto2 is None or cant_letras < punto2:
                    punto2 = cant_letras

            """Punto 3"""
            if tiene_g_en_pos_2 and not tiene_digito:
                acumulador_punto3 += cant_letras
                contador_punto3 += 1

            """Punto 4"""
            if tiene_pe and not empieza_con_vocal:
                punto4 += 1

            # Resteamos variables porque empieza otra palabra
            cant_letras = cant_consonantes = 0
            vocal_en_pos_2 = tiene_n = False
            tiene_g_en_pos_2 = tiene_digito = False
            empieza_con_vocal = tiene_pe = tiene_p = False

    punto3 = calcular_promedio(acumulador_punto3, contador_punto3)

    return punto1, punto2, punto3, punto4


def principal():
    with open("entrada_t6.txt") as archivo:
        r1, r2, r3, r4 = procesar_texto(archivo)

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == "__main__":
    principal()
