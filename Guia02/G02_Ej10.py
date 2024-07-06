# mensaje de inicio y carga de datos...
print('Calcular valor a pagar por película.')
total = float(input('Ingrese el total recaudado por la película: '))
nombre = input('Ingrese el nombre del participante: ')
porc = float(input('Indique el porcentaje a pagar: '))

# procesos...
monto = total * porc / 100

# resultados...
print('Se le debe pagar ', monto, ' pesos a ', nombre)