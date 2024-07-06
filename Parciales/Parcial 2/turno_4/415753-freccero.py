def es_vocal_menos_u(caracter):
    return caracter.upper() in "AEIO"


def procesar_archivo(archivo):
    cadena = archivo.read()

    punto_1 = 0
    punto_2 = None
    punto_3 = punto_4 = 0

    # Punto 1
    cant_carac_palabra = 0
    hay_carac_2da_pos = hay_carac_4ta_pos = hay_minuscula = False

    # Punto 2
    comienza_con_t = False
    menor_cant_carac = None

    # Punto 3
    palabra_solo_vocal_menos_u = True

    # Punto 4
    empieza_con_di = tiene_di = hay_d = False

    for car in cadena:
        if car != " " and car != ".":
            """Estamos analizando la palabra"""
            cant_carac_palabra += 1

            """Punto 1"""
            # Busco dígitos en la 2da y 4ta posición, y letras minúsculas
            if car.isdigit() and cant_carac_palabra == 2:
                hay_carac_2da_pos = True
            elif car.isdigit() and cant_carac_palabra == 4:
                hay_carac_4ta_pos = True
            elif car.islower():
                hay_minuscula = True

            """Punto 2"""
            # Busco que la letra palabra comience con una "t" mayúscula o minúscula
            if cant_carac_palabra == 1 and car in "Tt":
                comienza_con_t = True

            """Punto 3"""
            palabra_solo_vocal_menos_u = palabra_solo_vocal_menos_u and es_vocal_menos_u(car)

            """Punto 4"""
            if hay_d and car.upper() == "I":
                if cant_carac_palabra <= 2:
                    empieza_con_di = True
                tiene_di = True
            hay_d = car.upper() == "D"

        else:
            """Terminó la palabra"""
            """Punto 1"""
            if hay_carac_2da_pos and hay_carac_4ta_pos and not hay_minuscula:
                punto_1 += 1

            """Punto 2"""
            if comienza_con_t:
                if punto_2 is None or cant_carac_palabra < punto_2:
                    punto_2 = cant_carac_palabra

            """Punto 3"""
            if palabra_solo_vocal_menos_u:
                punto_3 += 1

            """Punto 4"""
            if tiene_di and not empieza_con_di:
                punto_4 += 1

            # Reseteamos las variables porque empieza otra palabra
            cant_carac_palabra = 0
            hay_carac_2da_pos = hay_carac_4ta_pos = hay_minuscula = False
            comienza_con_t = False
            palabra_solo_vocal_menos_u = True
            tiene_di = empieza_con_di = hay_d = False

    return punto_1, punto_2, punto_3, punto_4


def principal():
    with open("entrada.txt") as archivo:
        r1, r2, r3, r4 = procesar_archivo(archivo)

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == "__main__":
    principal()
