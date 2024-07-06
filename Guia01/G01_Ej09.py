#	Mensaje de inicio
print('Este programa calcula el área de un rectángulo en base a su perímetro y uno de sus lados.')

perim = float(input('Ingrese el perímetro del rectángulo: '))
lado1 = float(input('Ingrese el lado del rectángulo: '))
lado2 = (perim - lado1 * 2) / 2
area = lado1 * lado2

print('El área del rectángulo ingresado es: ', area)