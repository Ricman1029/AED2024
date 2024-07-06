# Programa para procesar un envío de correo

# Entrada de datos

cp = input("Ingrese el código postal del lugar de destino: ") 
direccion = input("Dirección del lugar de destino: ") 
tipo = int(input("Tipo de envío (id entre 0 y 6 - ver tabla 2 en el enunciado): ")) 
pago = int(input("Forma de pago (1: efectivo - 2: tarjeta): ")) 

# Procesamiento 
#procesamiento de país y provincia si corresponde
provincia = 'No aplica'

if len(cp) > 9:
    destino = 'Otros países'
elif len(cp) == 9 and cp[5]== '-':
    destino = 'Brasil'
elif len(cp) == 8:
    if cp[0] == 'A':
        destino = 'Argentina'
        provincia = 'Salta'
    elif cp[0] == 'B':
        destino = 'Argentina'
        provincia = 'Buenos Aires'
    elif cp[0] == 'C':
        destino = 'Argentina'
        provincia = 'Ciudad Autónoma de Buenos Aires'
    elif cp[0] == 'D':
        destino = 'Argentina'
        provincia = 'San Luis'
    elif cp[0] == 'E':
        destino = 'Argentina'
        provincia = 'Entre Ríos'
    elif cp[0] == 'F':
        destino = 'Argentina'
        provincia = 'La Rioja'
    elif cp[0] == 'G':
        destino = 'Argentina'
        provincia = 'Santiago del Estero'
    elif cp[0] == 'H':
        destino = 'Argentina'
        provincia = 'Chaco'
    elif cp[0] == 'J':
        destino = 'Argentina'
        provincia = 'San Juan'
    elif cp[0] == 'K':
        destino = 'Argentina'
        provincia = 'Catamarca'
    elif cp[0] == 'L':
        destino = 'Argentina'
        provincia = 'La Pampa'
    elif cp[0] == 'M':
        destino = 'Argentina'
        provincia = 'Mendoza'
    elif cp[0] == 'N':
        destino = 'Argentina'
        provincia = 'Misiones'
    elif cp[0] == 'P':
        destino = 'Argentina'
        provincia = 'Formosa'
    elif cp[0] == 'Q':
        destino = 'Argentina'
        provincia = 'Neuquén'
    elif cp[0] == 'R':
        destino = 'Argentina'
        provincia = 'Río Negro'
    elif cp[0] == 'S':
        destino = 'Argentina'
        provincia = 'Santa Fe'
    elif cp[0] == 'T':
        destino = 'Argentina'
        provincia = 'Tucumán'
    elif cp[0] == 'U':
        destino = 'Argentina'
        provincia = 'Chubut'
    elif cp[0] == 'V':
        destino = 'Argentina'
        provincia = 'Tierra del Fuego'
    elif cp[0] == 'W':
        destino = 'Argentina'
        provincia = 'Corrientes'
    elif cp[0] == 'X':
        destino = 'Argentina'
        provincia = 'Córdoba'
    elif cp[0] == 'Y':
        destino = 'Argentina'
        provincia = 'Jujuy'
    elif cp[0] == 'Z':
        destino = 'Argentina'
        provincia = 'Santa Cruz'
    else:
        destino = 'Otros países'
elif len(cp) == 7 and cp.isdigit():
    destino = 'Chile'
elif len(cp) == 6 and cp.isdigit():
    destino = 'Paraguay'
elif len(cp) == 5 and cp.isdigit():
    destino = 'Uruguay'
elif len(cp) == 4 and cp.isdigit():
    destino = 'Bolivia'
else:
    destino = 'Otros países'

#procesamiento de costo inicial

if tipo == 0:
    tarifa_inicial = 1100
elif tipo == 1:
    tarifa_inicial  = 1800
elif tipo == 2:
    tarifa_inicial  = 2450
elif tipo == 3:
    tarifa_inicial  = 8300
elif tipo == 4:
    tarifa_inicial  = 10900
elif tipo == 5:
    tarifa_inicial  = 14300
else:
    tarifa_inicial  = 17900
  

if destino == 'Argentina':
    print('entré por Argentina')
    inicial = tarifa_inicial
elif destino == 'Bolivia' or destino =='Paraguay':
    print('entré por Paraguay')
    inicial = tarifa_inicial * 1.2
elif destino == 'Uruguay':
    if direccion.find('Montevideo') != -1:
        print('Montevideo')
        inicial = tarifa_inicial * 1.2
    else:
        print('No Montevideo')
        inicial = tarifa_inicial * 1.25
elif destino == 'Chile':
    print('Entré por Chile')
    inicial = tarifa_inicial * 1.25
elif destino == 'Brasil':
    direccion = direccion.lower()
    print(direccion)
    if direccion.find('región 0') != -1 or direccion.find('región 1')!= -1 or direccion.find('región 2') != -1 or direccion.find('región 3') != -1:
        inicial = tarifa_inicial * 1.25
    elif direccion.find('región 4') != -1 or direccion.find('región 5') != -1 or direccion.find('región 6') != -1 or direccion.find('región 7') != -1:
        inicial = tarifa_inicial * 1.3
    else:
        inicial = tarifa_inicial * 1.2
else:
    inicial = tarifa_inicial * 1.5

# procesamiento de costo final 

if pago == 1:
    tarifa_final = inicial * 0.9
    final = int(tarifa_final)
else:
    final = inicial

# Impresión de datos

print("País de destino del envío:", destino) 
print("Provincia destino:", provincia) 
print("Importe inicial a pagar:", inicial) 
print("Importe final a pagar:", final)  