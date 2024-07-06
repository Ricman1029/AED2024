from funciones_tp1 import pais_e_importe_inicial


def obtener_control(archivo):
    timestamp = archivo.readline()
    if "HC" in timestamp:
        return "Hard Control"
    return "Soft Control"


def obtener_codigo_postal(cadena):
    codigo = ""
    # Los caracteres de 0 al 8 indican el código postal del envío
    i = 0
    while i <= 8:
        if cadena[i] != " ":
            codigo += cadena[i]
        i += 1
    return codigo


def obtener_direccion(cadena):
    direccion = ""
    # Los caracteres del 9 al 28 indican la dirección del destino
    i = 9
    while i <= 28:
        direccion += cadena[i]
        i += 1
    return direccion


def obtener_datos_envio(cadena):
    codigo_postal = obtener_codigo_postal(cadena)
    direccion = obtener_direccion(cadena)
    tipo_envio = cadena[29]
    forma_pago = cadena[30]

    return codigo_postal, direccion, tipo_envio, forma_pago


def validar_envio(cadena):
    # Si el envío es válido, retornamos el número 1 para poder sumarlo, sino retornamos 0.
    hay_mayuscula = hay_letra = hay_palabra_digitos = False

    for car in cadena:
        # Si estamos analizando una palabra
        if car != " " and car != ".":
            # Si la cadena tiene algún caracter que no es ni letra ni digito, el envío NO es válido
            if not car.isdigit() and not car.isalpha():
                return False

            # Si hay dos mayúsculas seguidas, el envío NO es válido
            if hay_mayuscula and car.isupper():
                return False
            hay_mayuscula = False
            # Si el caracter es una mayúscula, levantamos una bandera
            if car.isupper():
                hay_mayuscula = True

            # Si hay una letra en la palabra, levantamos una bandera
            if car.isalpha():
                hay_letra = True

        # Si car es un espacio, significa que terminó una palabra
        elif car == " " or car == ".":
            # Si la palabra que terminó estaba compuesta solo por dígitos, levantamos una bandera
            if not hay_letra:
                hay_palabra_digitos = True

            # Reseteamos el resto de las variables ya que empieza una nueva palabra
            hay_mayuscula = hay_letra = False

        # Si car es un punto, significa que terminó la dirección
        elif car == ".":
            if not hay_palabra_digitos:
                return False

    return True


def calcular_importe_final(inicial, forma_pago):
    if forma_pago == "1":
        return int(inicial * 0.9)
    return inicial


def contar_tipo_envios(tipo_envio, tipo1, tipo2, tipo3):
    if tipo_envio in "012":
        tipo1 += 1
    elif tipo_envio in "34":
        tipo2 += 1
    else:
        tipo3 += 1

    return tipo1, tipo2, tipo3


def mayor_tipo_envios(tipo1, tipo2, tipo3):
    if tipo1 > tipo2 and tipo1 > tipo3:
        return "Carta Simple"
    if tipo2 > tipo3:
        return "Carta Certificada"
    return "Carta Expresa"


def menor_importe_brasil(actual, menor):
    if actual[0] < menor[0]:
        return actual
    return menor


def envio_buenos_aires(codigo):
    if codigo[0] == "B":
        return True
    return False


def procesar_archivo(archivo):
    global control, cedvalid, cedinvalid, imp_acu_total, ccs, ccc, cce, \
        tipo_mayor, primer_cp, cant_primer_cp, menimp, mencp, porc, prom

    # r1
    control = obtener_control(archivo)
    # r2 y r3
    cedvalid = cedinvalid = cont_envios_totales = 0
    # r4
    imp_acu_total = 0
    # r5, r6 y r7
    ccs = ccc = cce = 0
    # r10
    cant_primer_cp = 0
    # r11 y r12
    menimp = None
    # r13
    envios_exterior = 0
    # r14
    imp_final_bs_as = cont_envios_bs_as = 0

    # Comenzamos a leer todas las líneas del archivo
    linea = archivo.readline()
    primer_cp = obtener_codigo_postal(linea)
    while linea != "":
        # Contamos cada envío realizado
        cont_envios_totales += 1
        # Obtenemos los datos de los envíos
        codigo_postal, direccion, tipo_envio, forma_pago = obtener_datos_envio(linea)
        # Obtenemos el pais y el importe inicial del envío
        pais, importe_inicial = pais_e_importe_inicial(codigo_postal, tipo_envio)
        # Calculamos el importe final
        importe_final = calcular_importe_final(importe_inicial, forma_pago)

        # Realizamos acciones dependiendo del tipo de control
        if control == "Hard Control":
            if validar_envio(direccion):
                # Contamos los envíos con dirección válida
                cedvalid += 1
                # Acumulamos los importes finales de los envíos con dirección válida
                imp_acu_total += importe_final
                # Contamos los tipos de envíos con dirección válida
                ccs, ccc, cce = contar_tipo_envios(tipo_envio, ccs, ccc, cce)
                # Contamos la cantidad de envíos que fueron al exterior con una dirección válida
                if pais != "Argentina":
                    envios_exterior += 1
                else:
                    # Sumamos los importes finales de los envíos que iban a Buenos Aires con dirección válida
                    if envio_buenos_aires(codigo_postal):
                        imp_final_bs_as += importe_final
                        cont_envios_bs_as += 1

        else:
            # Contamos los envíos
            cedvalid += 1
            # Acumulamos los importes finales de los envíos
            imp_acu_total += importe_final
            # Contamos los tipos de envíos
            ccs, ccc, cce = contar_tipo_envios(tipo_envio, ccs, ccc, cce)
            # Contamos la cantidad de envíos que fueron al exterior con una dirección válida
            if pais != "Argentina":
                envios_exterior += 1
            else:
                # Sumamos los importes finales de los envíos que iban a Buenos Aires
                if envio_buenos_aires(codigo_postal):
                    imp_final_bs_as += importe_final
                    cont_envios_bs_as += 1

        # Contamos la cantidad de veces que el primer código postal aparece en el archivo
        if primer_cp == codigo_postal:
            cant_primer_cp += 1

        # Buscamos el menor importe final pagado por un envío a Brasil y su código postal
        if pais == "Brasil":
            if menimp is None:
                menimp, mencp = importe_final, codigo_postal
            else:
                menimp, mencp = menor_importe_brasil((importe_final, codigo_postal), (menimp, mencp))

        # Buscamos el siguiente envío
        linea = archivo.readline()

    # Calculamos la cantidad de envíos inválidos
    cedinvalid = cont_envios_totales - cedvalid

    # Determinamos el tipo de carta con mayor cantidad de envíos
    tipo_mayor = mayor_tipo_envios(ccs, ccc, cce)

    # Calculamos el porcentaje de envíos al exterior sobre el total de envíos
    if cont_envios_totales != 0:
        porc = int(envios_exterior * 100 / cont_envios_totales)
    else:
        porc = 0

    # Calculamos el monto final promedio pagado por los envíos a Buenos Aires
    if cont_envios_bs_as != 0:
        prom = int(imp_final_bs_as / cont_envios_bs_as)
    else:
        prom = 0


def imprimir_resultados():
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

def principal():
    # Primero abrimos el archivo para poder leerlo
    with open("envios25.txt") as archivo:
        procesar_archivo(archivo)

    # Imprimimos los resultados obtenidos
    imprimir_resultados()


if __name__ == "__main__":
    principal()
