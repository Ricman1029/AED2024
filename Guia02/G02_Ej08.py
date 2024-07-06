# mensaje de inicio y carga de datos...
print('Calcular cantidad de quintales de trigo posibles a producir.')
largo = float(input('Ingrese el largo de su parcela en metros: '))
ancho = float(input('Ingrese el ancho de su parcela en metros: '))

# procesos...
area = largo * ancho
cant = area // 10 * 2   # puse división entera porque no puede tener una porcion de quintal

# resultados...
print('Usted puede producir en total ', cant, 'quintales por parcela.')