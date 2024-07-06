#	Mensaje de inicio
print('Este programa convierte una medida en pies a yardas, pulgadas, centímetros y metros')

pies = float(input('Ingrese la medida en pies: '))

yardas = pies / 3
pulgada = 12 * pies
centi = pulgada * 2.54
metro = centi / 100

print(pies, 'pie/s quivalen a:')
print('Yardas: ', yardas)
print('Pulgadas: ', pulgada)
print('Centímetros: ', centi)
print('Metros: ', metro)