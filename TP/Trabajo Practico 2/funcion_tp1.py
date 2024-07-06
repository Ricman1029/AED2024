def funciones_tp1(cp, tipo, pago):
    # Se determina el precio inicial en base al tipo de envío
    precio = 1100, 1800, 2450, 8300, 10900, 14300, 17900
    inicial = precio[tipo]

    # Valor por defecto de provincia.
    # Solo se cambia si el envío va al interior de Argentina
    provincia = "No aplica"

    # Bolivia tiene 4 dígitos y todos números
    if len(cp) == 4 and "0" <= cp[0] <= "9" \
            and "0" <= cp[1] <= "9" \
            and "0" <= cp[2] <= "9" \
            and "0" <= cp[3] <= "9":
        # Se le agrega un 20%
        destino = "Bolivia"
        inicial = int(inicial * 1.20)

    # Chile tiene 7 dígitos y todos números
    elif len(cp) == 7 and "0" <= cp[0] <= "9" \
            and "0" <= cp[1] <= "9" \
            and "0" <= cp[2] <= "9" \
            and "0" <= cp[3] <= "9" \
            and "0" <= cp[4] <= "9" \
            and "0" <= cp[5] <= "9" \
            and "0" <= cp[6] <= "9":
        # Se le agrega un 25%
        destino = "Chile"
        inicial = int(inicial * 1.25)

    # Paraguay tiene 6 dígitos y todos números
    elif len(cp) == 6 and ("0" <= cp[0] <= "9") \
            and "0" <= cp[1] <= "9" \
            and "0" <= cp[2] <= "9" \
            and "0" <= cp[3] <= "9" \
            and "0" <= cp[4] <= "9" \
            and "0" <= cp[5] <= "9":
        # Se le agrega un 20%
        destino = "Paraguay"
        inicial = int(inicial * 1.20)

    # Uruguay tiene 5 dígitos y todos números
    elif len(cp) == 5 and "0" <= cp[0] <= "9" \
            and "0" <= cp[1] <= "9" \
            and "0" <= cp[2] <= "9" \
            and "0" <= cp[3] <= "9" \
            and "0" <= cp[4] <= "9":
        destino = "Uruguay"
        # Si el primer dígito es un 1, es Montevideo
        # Y se le agrega un 20%
        if cp[0] == "1":
            inicial = int(inicial * 1.20)
        # Sino, NO es de Montevideo
        # Y se le agrega un 25%
        else:
            inicial = int(inicial * 1.25)

    # Argentina tiene 8 caracteres y EL PRIMER CARACTER ES UNA LETRA (distinta de "I" u "O")
    # Además los primeros 4 caracteres después de la 1er letra son números
    # Y los últimos 3 caracteres son letras
    elif len(cp) == 8 and "A" <= cp[0] <= "Z" and (cp[0] != "I" and cp[0] != "O") \
            and "0" <= cp[1] <= "9" \
            and "0" <= cp[2] <= "9" \
            and "0" <= cp[3] <= "9" \
            and "0" <= cp[4] <= "9" \
            and "A" <= cp[5] <= "Z" \
            and "A" <= cp[6] <= "Z" \
            and "A" <= cp[7] <= "Z":
        destino = "Argentina"

        # Indica la provincia de Argentina según el ISO 3166-2:AR
        if cp[0] == "A":
            provincia = "Salta"
        elif cp[0] == "B":
            provincia = "Buenos Aires"
        elif cp[0] == "C":
            provincia = "Ciudad Autónoma de Buenos Aires"
        elif cp[0] == "D":
            provincia = "San Luis"
        elif cp[0] == "E":
            provincia = "Entre Ríos"
        elif cp[0] == "F":
            provincia = "La Rioja"
        elif cp[0] == "G":
            provincia = "Santiago del Estero"
        elif cp[0] == "H":
            provincia = "Chaco"
        elif cp[0] == "J":
            provincia = "San Juan"
        elif cp[0] == "K":
            provincia = "Catamarca"
        elif cp[0] == "L":
            provincia = "La Pampa"
        elif cp[0] == "M":
            provincia = "Mendoza"
        elif cp[0] == "N":
            provincia = "Misiones"
        elif cp[0] == "P":
            provincia = "Formosa"
        elif cp[0] == "Q":
            provincia = "Neuquén"
        elif cp[0] == "R":
            provincia = "Río Negro"
        elif cp[0] == "S":
            provincia = "Santa Fe"
        elif cp[0] == "T":
            provincia = "Tucumán"
        elif cp[0] == "U":
            provincia = "Chubut"
        elif cp[0] == "V":
            provincia = "Tierra del Fuego"
        elif cp[0] == "W":
            provincia = "Corrientes"
        elif cp[0] == "X":
            provincia = "Córdoba"
        elif cp[0] == "Y":
            provincia = "Jujuy"
        else:
            provincia = "Santa Cruz"

    # Brasil tiene 9 caracteres y EL SEXTO CARACTER ES UN GUIÓN "-"
    # Además los primeros 5 caracteres tienen que ser números
    # Y los últimos 3 caracteres tienen que ser números
    elif len(cp) == 9 and cp[5] == "-" \
            and "0" <= cp[0] <= "9" \
            and "0" <= cp[1] <= "9" \
            and "0" <= cp[2] <= "9" \
            and "0" <= cp[3] <= "9" \
            and "0" <= cp[4] <= "9" \
            and "0" <= cp[6] <= "9" \
            and "0" <= cp[7] <= "9" \
            and "0" <= cp[8] <= "9":
        destino = "Brasil"
        # El primer dígito del cp de Brasil indica la región
        # Si el primer dígito es 8 o 9, se agrega un 20%
        if cp[0] == "8" or cp[0] == "9":
            inicial = int(inicial * 1.20)
        # Si el primer dígito está entre 0 y 3, se agrega un 25%
        elif 0 <= int(cp[0]) <= 3:
            inicial = int(inicial * 1.25)
        # Si el primer dígito está entre 4 y 7, se agrega un 30%
        else:
            inicial = int(inicial * 1.30)

    # Sino cumple con ninguna de las condiciones anteriores, es otro pais.
    else:
        destino = "Otro"
        inicial = int(inicial * 1.5)

    # Si el usuario pagó en efectivo se le descuenta el 10%
    if pago == 1:
        final = int(inicial * 0.9)
    # Sino, no se le descuenta nada
    else:
        final = inicial

    