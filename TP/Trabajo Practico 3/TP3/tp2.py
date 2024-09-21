def determinar_control(linea):
    if "HC" in linea:
        return "Hard Control"
    elif "SC" in linea:
        return "Soft Control"


def validacion_envios(envio):
    # Solo tiene que tener letras y dígitos
    # No pueden haber dos mayúsculas seguidas
    # Tiene que haber una palabra solo compuesta por dígitos
    una_mayuscula = False
    hay_letra = palabra_solo_digitos = False

    for caracter in envio:
        # Si estamos adentro de una palabra
        if caracter != " " and caracter != ".":
            # Si tiene algún caracter que NO es una letra o un dígito, entonces el envío es inválido
            if not ("a" <= caracter <= "z" or "A" <= caracter <= "Z" or "0" <= caracter <= "9"):
                return False

            # Si hay dos mayúsculas seguidas, entonces el envío es inválido
            if una_mayuscula and "A" <= caracter <= "Z":
                return False
            elif "A" <= caracter <= "Z":
                una_mayuscula = True
            else:
                una_mayuscula = False

            # Nos fijamos si el caracter es un dígito o no.
            if not ("0" <= caracter <= "9"):
                hay_letra = True

        # Si terminó la palabra y NO había una letra, entonces la palabra era de solo dígitos
        elif caracter == " " or caracter == ".":
            if not hay_letra:
                palabra_solo_digitos = True

            # Reseteamos la variable porque empieza otra palabra
            hay_letra = False
        # Si terminó la dirección y NO había una palabra de solo dígitos, entonces es inválido
        if caracter == "." and not palabra_solo_digitos:
            return False

    return True


def obtener_codigo_postal(linea):
    posicion = 0
    codigo_postal = ""

    while posicion <= 8:
        if linea[posicion] != " ":
            codigo_postal += linea[posicion]
        posicion += 1

    return codigo_postal


def obtener_direccion(linea):
    posicion = 9
    direccion = ""
    
    while posicion <= 28 and linea[posicion] != ".":
        direccion += linea[posicion]
        posicion += 1
    direccion += "."

    return direccion


def obtener_tipo_envio(linea):
    return linea[29]


def obtener_forma_pago(linea):
    return linea[30]


# Resultado 4

"""LAS SIG 2 LÍNEAS LAS COMENTÓ RICARDO PORQUE NO SE USABAN, EN LA PUMA LAS VEMOS"""
# imp_acu_total = 0
# c_carta_simple = c_carta_certificado = c_carta_expresa = 0

"""RICARDO CAMBIÓ EL NOMBRE PORQUE TENÍAMOS UNA VARIABLE LLAMADA IGUAL QUE LA FUNCIÓN"""


def funcion_codigo_postal(cp, tipo_envio):
    # Se determina el precio importe_inicial en base al tipo de envío
    precio = 1100, 1800, 2450, 8300, 10900, 14300, 17900
    """
    CAMBIO TEMPORAL, AGREGUÉ EL PARÁMETRO "TIPO"
    """
    importe_inicial = precio[tipo_envio]
    # importe_inicial = precio[tipo_envio()]
    """
    TERMINA CAMBIO TEMPORAL
    """
    if len(cp) == 8 and "A" <= cp[0] <= "Z" and (cp[0] != "I" and cp[0] != "O") \
            and "0" <= cp[1] <= "9" \
            and "0" <= cp[2] <= "9" \
            and "0" <= cp[3] <= "9" \
            and "0" <= cp[4] <= "9" \
            and "A" <= cp[5] <= "Z" \
            and "A" <= cp[6] <= "Z" \
            and "A" <= cp[7] <= "Z":
        destino = "Argentina"
        return destino, importe_inicial

    # Brasil
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
    # ACÁ DECÍA IF, RICARDO PUSO ELIF
    elif len(cp) == 4 and cp.isdigit():
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

    # ACA AGREGO "OTROS" POR SI EL CÓDIGO POSTAL NO PERTENECE A NINGÚN PAÍS
    else:
        destino = "Otros"
        importe_inicial = int(importe_inicial * 1.5)
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
    if num1 >= num2 and num1 >= num3:
        return "Carta Simple"
    elif num2 >= num3:
        return "Carta Certificada"
    else:
        return "Carta Expresa"


# Resultado 9 y 10
# Guardar el primer codigo postal y contar cuantas veces aparecio en total
def contar_cp(primer_cp, cp_actual):
    if cp_actual == primer_cp:
        return 1
    return 0



# Resultado 11 y 12
def impor_do_menor_do_brasil(final, menor):

    if final[0] < menor[0]:
        menor = final
        return menor
    return menor


def contador_carta(tipo, ccs, ccc, cce):
    if 0 <= tipo <= 2:
        ccs += 1
    elif 3 <= tipo <= 4:
        ccc += 1
    else:
        cce += 1

    return ccs, ccc, cce


def porcentaje(envio, contador_total_envios):
    return int((envio * 100) / contador_total_envios)


def chequear_envio_bsas(cp):
    if cp[0] == "B":
        return True


def promedio(acumulador,contador):
    return int(acumulador / contador)


def principal():
    # r2 y r3
    cedvalid, cedinvalid = 0, 0
    # r4
    pais, importe_inicial = 0, 0
    imp_acu_total = 0
    # r5, r6, r7
    ccs = ccc = cce = 0
    # r10
    cant_primer_cp = 0
    # r11 y r12
    primer_envio_brasil = False
    # r13
    contador_total_envios = contador_ext_envios = 0
    # r14
    contador_bsas = acumulador_bsas = 0

    archivo = open("envios100HC.txt", "r")

    # Leemos la primer línea para determinar el tipo de control
    primer_linea = archivo.readline()
    control = determinar_control(primer_linea)

    linea = archivo.readline()
    primer_cp = obtener_codigo_postal(linea)
    while linea != "":
        codigo_postal = obtener_codigo_postal(linea)
        direccion = obtener_direccion(linea)
        tipo_envio = int(obtener_tipo_envio(linea))
        forma_pago = int(obtener_forma_pago(linea))
        pais, importe_inicial = funcion_codigo_postal(codigo_postal, tipo_envio)
        imp_final = importe_final(importe_inicial, forma_pago)

        if control == "Hard Control":
            if validacion_envios(direccion):
                cedvalid += 1
                # Actualizamos la suma de los importes finales
                imp_acu_total += imp_final
                ccs, ccc, cce = contador_carta(tipo_envio, ccs, ccc, cce)

                if pais == "Argentina" and chequear_envio_bsas(codigo_postal):
                    contador_bsas += 1
                    acumulador_bsas += imp_final
                if pais != "Argentina":
                    contador_ext_envios += 1
            else:
                cedinvalid += 1
        else:
            cedvalid += 1
            # Actualizamos la suma de los importes finales
            imp_acu_total += imp_final
            ccs, ccc, cce = contador_carta(tipo_envio, ccs, ccc, cce)

            if pais == "Argentina" and chequear_envio_bsas(codigo_postal):
                contador_bsas += 1
                acumulador_bsas += imp_final
            if pais != "Argentina":
                contador_ext_envios += 1

        if pais == "Brasil" and not primer_envio_brasil:
            menimp = imp_final
            mencp = codigo_postal
            primer_envio_brasil = True

        elif pais == "Brasil":
            menimp, mencp = impor_do_menor_do_brasil((imp_final, codigo_postal), (menimp, mencp))

        cant_primer_cp += contar_cp(primer_cp, codigo_postal)
        contador_total_envios += 1
        linea = archivo.readline()

    tipo_mayor = mayor_cant_envio(ccs, ccc, cce)
    porc = porcentaje(contador_ext_envios, contador_total_envios)
    prom = promedio(acumulador_bsas, contador_bsas)

    print(' (r1) - Tipo de control de direcciones:', control)
    print(' (r2) - Cantidad de envios con direccion valida:', cedvalid)
    print(' (r3) - Cantidad de envios con direccion no valida:', cedinvalid)
    print(' (r4) - Total acumulado de importes finales:', imp_acu_total)
    print(' (r5) - Cantidad de cartas simples:', ccs)
    print(' (r6) - Cantidad de cartas certificadas:', ccc)
    print(' (r7) - Cantidad de cartas expresas:', cce)
    print(' (r8) - Tipo de carta con mayor cantidad de envios:', tipo_mayor)
    print(' (r9) - Codigo postal del primer envio del archivo:', primer_cp)
    print('(r10) - Cantidad de veces que entro ese primero:', cant_primer_cp)
    print('(r11) - Importe menor pagado por envios a Brasil:', menimp)
    print('(r12) - Codigo postal del envio a Brasil con importe menor:', mencp)
    print('(r13) - Porcentaje de envios al exterior sobre el total:', porc)
    print('(r14) - Importe final promedio de los envios Buenos Aires:', prom)


if __name__ == "__main__":
    principal()
