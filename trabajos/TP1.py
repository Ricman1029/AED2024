# Carga de datos
cp = input("Ingrese el código postal del lugar de destino: ")
direccion = input("Dirección del lugar de destino: ")
tipo = int(input("Tipo de envío (id entre 0 y 6 - ver tabla 2 en el enunciado): "))
pago = int(input("Forma de pago (1: efectivo - 2: tarjeta): "))

# Se determina el precio inicial en base al tipo de envío
if tipo == 0:
    inicial = 1100
elif tipo == 1:
    inicial = 1800
elif tipo == 2:
    inicial = 2450
elif tipo == 3:
    inicial = 8300
elif tipo == 4:
    inicial = 10900
elif tipo == 5:
    inicial = 14300
else:
    inicial = 17900

# Valor por defecto de provincia.
# Solo se cambia si el envío va al interior de Argentina
provincia = "No aplica"

# Bolivia tiene 4 dígitos y todos números
if len(cp) == 4 and "0000" <= cp <= "9999":
    # Se le agrega un 20%
    destino = "Bolivia"
    inicial = int(inicial * 1.20)

# Chile tiene 7 dígitos y todos números
elif len(cp) == 7 and "0000000" <= cp <= "9999999":
    # Se le agrega un 25%
    destino = "Chile"
    inicial = int(inicial * 1.25)

# Paraguay tiene 6 dígitos y todos números
elif len(cp) == 6 and "000000" <= cp <= "999999":
    # Se le agrega un 20%
    destino = "Paraguay"
    inicial = int(inicial * 1.20)

# Uruguay tiene 5 dígitos y todos números
elif len(cp) == 5 and "00000" <= cp <= "99999":
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
elif len(cp) == 8 and "A" <= cp[0] <= "Z" and (cp[0] != "I" and cp[0] != "O")\
        and "0000" <= (cp[1] + cp[2] + cp[3] + cp[4]) <= "9999"\
        and "AAA" <= (cp[5] + cp[6] + cp[7]) <= "ZZZ":
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
elif len(cp) == 9 and cp[5] == "-"\
        and "00000" <= (cp[0] + cp[1] + cp[2] + cp[3] + cp[4]) <= "99999"\
        and "000" <= (cp[6] + cp[7] + cp[8]) <= "999":
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

# Muestra de datos
print("País de destino del envío:", destino)
print("Provincia destino:", provincia)
print("Importe inicial a pagar:", inicial)
print("Importe final a pagar:", final)
