def pais_destino(cp):
    largo = len(cp)

    # Iniciamos país como Otro
    pais = 'Otro'

    # Puede ser Argentina
    if largo == 8:
        # Si es Argentina, cambiamos el nombre de pais
        if cp[0].isalpha() and cp[0] not in 'IO' and cp[1:5].isdigit() and cp[5:8].isalpha():
            pais = 'Argentina'

    # Puede ser Brasil
    if largo == 9:
        # Si es Brasil, cambiamos el nombre de pais
        if cp[0:5].isdigit() and cp[5] == '-' and cp[6:9].isdigit():
            pais = 'Brasil'

    if cp.isdigit():
        # Si es Bolivia, cambiamos el nombre de pais
        if largo == 4:
            pais = 'Bolivia'

        # Si es Chile, cambiamos el nombre de pais
        if largo == 7:
            pais = 'Chile'

        # Si es Paraguay, cambiamos el nombre de pais
        if largo == 6:
            pais = 'Paraguay'

        # Si es Uruguay, cambiamos el nombre de pais
        if largo == 5:
            pais = 'Uruguay'

    # Devolvemos el valor que haya en la variable pais
    return pais

def determinar_importe_final(cp, destino, tipo, pago):
    # determinación del importe importe_inicial a pagar.
    precio = (1100, 1800, 2450, 8300, 10900, 14300, 17900)
    importe_inicial = precio[tipo]

    if destino == 'Bolivia' or destino == 'Paraguay' or (destino == 'Uruguay' and cp[0] == '1'):
        importe_inicial = int(importe_inicial * 1.20)
    elif destino == 'Chile' or (destino == 'Uruguay' and cp[0] != '1'):
        importe_inicial = int(importe_inicial * 1.25)
    elif destino == 'Brasil':
        if cp[0] == '8' or cp[0] == '9':
            importe_inicial = int(importe_inicial * 1.20)
        else:
            if cp[0] == '0' or cp[0] == '1' or cp[0] == '2' or cp[0] == '3':
                importe_inicial = int(importe_inicial * 1.25)
            else:
                importe_inicial = int(importe_inicial * 1.30)
    elif destino != 'Argentina':
        importe_inicial = int(importe_inicial * 1.50)

    if pago == 1:
        final = int(0.9 * importe_inicial)
        return final

    return importe_inicial
            
            
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

    while posicion <= 28:
        direccion += linea[posicion]
        posicion += 1

    return direccion


def obtener_tipo_envio(linea):
    return linea[29]


def obtener_forma_pago(linea):
    return linea[30]

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

###################################################################################################################

