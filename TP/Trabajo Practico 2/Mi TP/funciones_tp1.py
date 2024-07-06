def es_bolivia(codigo_postal):
    return len(codigo_postal) == 4 \
            and "0" <= codigo_postal[0] <= "9"\
            and "0" <= codigo_postal[1] <= "9"\
            and "0" <= codigo_postal[2] <= "9"\
            and "0" <= codigo_postal[3] <= "9"


def es_chile(codigo_postal):
    return len(codigo_postal) == 7 \
            and "0" <= codigo_postal[0] <= "9" \
            and "0" <= codigo_postal[1] <= "9" \
            and "0" <= codigo_postal[2] <= "9" \
            and "0" <= codigo_postal[3] <= "9" \
            and "0" <= codigo_postal[4] <= "9" \
            and "0" <= codigo_postal[5] <= "9" \
            and "0" <= codigo_postal[6] <= "9"


def es_paraguay(codigo_postal):
    return len(codigo_postal) == 6 \
            and ("0" <= codigo_postal[0] <= "9") \
            and "0" <= codigo_postal[1] <= "9" \
            and "0" <= codigo_postal[2] <= "9" \
            and "0" <= codigo_postal[3] <= "9" \
            and "0" <= codigo_postal[4] <= "9" \
            and "0" <= codigo_postal[5] <= "9"


def es_uruguay(codigo_postal):
    return len(codigo_postal) == 5 \
            and "0" <= codigo_postal[0] <= "9" \
            and "0" <= codigo_postal[1] <= "9" \
            and "0" <= codigo_postal[2] <= "9" \
            and "0" <= codigo_postal[3] <= "9" \
            and "0" <= codigo_postal[4] <= "9"


def es_argentina(codigo_postal):
    return len(codigo_postal) == 8 and "A" <= codigo_postal[0] <= "Z" \
            and (codigo_postal[0] != "I" and codigo_postal[0] != "O") \
            and "0" <= codigo_postal[1] <= "9" \
            and "0" <= codigo_postal[2] <= "9" \
            and "0" <= codigo_postal[3] <= "9" \
            and "0" <= codigo_postal[4] <= "9" \
            and "A" <= codigo_postal[5] <= "Z" \
            and "A" <= codigo_postal[6] <= "Z" \
            and "A" <= codigo_postal[7] <= "Z"


def es_brasil(codigo_postal):
    return len(codigo_postal) == 9 and codigo_postal[5] == "-"\
            and "0" <= codigo_postal[0] <= "9"\
            and "0" <= codigo_postal[1] <= "9"\
            and "0" <= codigo_postal[2] <= "9"\
            and "0" <= codigo_postal[3] <= "9"\
            and "0" <= codigo_postal[4] <= "9"\
            and "0" <= codigo_postal[6] <= "9"\
            and "0" <= codigo_postal[7] <= "9"\
            and "0" <= codigo_postal[8] <= "9"


def pais_e_importe_inicial(codigo_postal, tipo):
    precio = 1100, 1800, 2450, 8300, 10900, 14300, 17900
    importe_inicial = precio[int(tipo)]

    if es_bolivia(codigo_postal):
        destino = "Bolivia"
        importe_inicial = int(importe_inicial * 1.2)

    elif es_chile(codigo_postal):
        destino = "Chile"
        importe_inicial = int(importe_inicial * 1.25)

    elif es_paraguay(codigo_postal):
        destino = "Paraguay"
        importe_inicial = int(importe_inicial * 1.2)

    elif es_uruguay(codigo_postal):
        destino = "Uruguay"
        if codigo_postal[0] == "1":
            importe_inicial = int(importe_inicial * 1.2)
        else:
            importe_inicial = int(importe_inicial * 1.25)

    elif es_argentina(codigo_postal):
        destino = "Argentina"

    elif es_brasil(codigo_postal):
        destino = "Brasil"
        if codigo_postal[0] in "89":
            importe_inicial = int(importe_inicial * 1.2)
        elif codigo_postal[0] in "0123":
            importe_inicial = int(importe_inicial * 1.25)
        else:
            importe_inicial = int(importe_inicial * 1.3)

    else:
        destino = "Otro"
        importe_inicial = int(importe_inicial * 1.5)

    return destino, importe_inicial

