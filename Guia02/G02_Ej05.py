# carga de datos...
x = float(input('Ingrese el valor x: '))
y = float(input('Ingrese el valor y: '))

# procesos...
# alpha + beta = x
# alpha - beta = y

# alpha = x - beta
# x - 2beta = y
# beta = (x - y) / 2
# alpha = x - beta
beta = (x - y) / 2
alpha = x - beta

# resultados...
print('Alpha: ', alpha, '- Beta: ', beta)
