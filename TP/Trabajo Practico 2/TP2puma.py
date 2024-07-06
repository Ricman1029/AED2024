# Resultado 4

# ESTAS LAS COMENTÓ RICARDO PORQUE NO SE USABAN, EN LA PUMA LAS VEMOS
# imp_acu_total = 0
# c_carta_simple = c_carta_certificado = c_carta_expresa = 0


def codigo_postal(cp):
    # Se determina el precio importe_inicial en base al tipo de envío
    precio = 1100, 1800, 2450, 8300, 10900, 14300, 17900
    importe_inicial = precio[tipo_envio()]
    if len(cp) == 8 and "A" <= cp[0] <= "Z" and (cp[0] != "I" and cp[0] != "O")\
        and ((cp[1] and cp[2] and cp[3] and cp[4]).isdigit())\
            and 'A' <= (cp[5] and cp[6] and cp[7]) <= 'Z':
        destino = "Argentina"
        provincia = 'Interior'
        if cp[0] == "B":
            provincia = "Buenos Aires"
        return provincia, destino, importe_inicial

    # Brasil
    elif (len(cp) == 9 and cp[5] == "-"
          and (cp[0] and cp[1] and cp[2] and cp[3] and cp[4] and cp[6] and cp[7] and cp[8]).isdigit()):
        destino = "Brasil"
    # El primer dígito del cp de Brasil indica la región
    # Si el primer dígito es 8 o 9, se agrega un 20%
        if cp[0] == "8" or cp[0] == "9":
            importe_inicial = int(importe_inicial * 1.20)
        # Si el primer dígito está entre 0 y 3, se agrega un 25%
        elif 0 <= int(cp[0]) <= 3:
            importe_inicial = int(importe_inicial * 1.25)
        # Si el primer dígito está entre 4 y 7, se agrega un 30%
        else:
            importe_inicial = int(importe_inicial * 1.30)
        return destino, importe_inicial
        # Uruguay tiene 5 dígitos y todos números
    elif len(cp) == 5 and cp.isdigit():
        destino = "Uruguay"
        # Si el primer dígito es un 1, es Montevideo
        # Y se le agrega un 20%
        if cp[0] == "1":
            importe_inicial = int(importe_inicial * 1.20)
        # Sino, NO es de Montevideo
        # Y se le agrega un 25%
        else:
            importe_inicial = int(importe_inicial * 1.25)
        return destino, importe_inicial

        # Paraguay tiene 6 dígitos y todos números
    elif len(cp) == 6 and cp.isdigit():
        # Se le agrega un 20%
        destino = "Paraguay"
        importe_inicial = int(importe_inicial * 1.20)
        return destino, importe_inicial

    # Bolivia tiene 4 dígitos y todos números
    if len(cp) == 4 and cp.isdigit():
        # Se le agrega un 20%
        destino = "Bolivia"
        importe_inicial = int(importe_inicial * 1.20)
        return destino, importe_inicial

    # Chile tiene 7 dígitos y todos números
    elif len(cp) == 7 and cp.isdigit():
        # Se le agrega un 25%
        destino = "Chile"
        importe_inicial = int(importe_inicial * 1.25)
        return destino, importe_inicial


def importe_final(importe_inicial, metodo_pago):
    if metodo_pago == 1:
        final = int(importe_inicial * 0.9)
      #  if direccion_valida:
          #  acumulador_importes += final
        return final
        # esto hay que corregirlo asi a partir del destino calcula el importe
        # dependiendo si es hc o sc
    else:
        return importe_inicial

# Resultado 8
def mayor_cant_envio(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3:
        return num2
    else:
        return num3

# Resultado 9 y 10
# Guardar el primer codigo postal y contar cuantas veces aparecio en total
def contar_cp(primer_cp,cp_actual):
    cp_repetido = 0
    if cp_actual == primer_cp:
        cp_repetido += 1

# Resultado 11 y 12
def impor_do_menor_do_brasil(menor, final, cp):
    if final < menor:
        menor = final

# Resultado 13

def destino_envio(cp):
    if cp != "Argentina":
        return 1
    return 0
    # contador total de envios

def porcentaje(envio, contador_total_envios):
    return int((envio * 100) / contador_total_envios)


# Resultado 14









