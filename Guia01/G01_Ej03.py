#	Mensaje de inicio
print('Este programa calcula el área de un triángulo cuya altura es igual al cuadrado de su base.')

base = float(input('Indique la base del triángulo: '))
altura = base ** 2
area = base * altura / 2

print('El área del triángulo de base ', base, ' y altura ', altura, ' es igual a: ', area)