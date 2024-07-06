# mensaje de inicio y carga de datos...
print('Definir resultado de votación')
favor = int(input('Ingrese la cantidad de votos a favor: '))
contra = int(input('Ingrese la cantidad de votos en contra: '))

# procesos...
# favor + contra = 100% (determinar porcentaje de favor y contra)
total = favor + contra
pf = favor * 100 / total
pc = contra * 100 / total

# resultados...
print('Porcentaje a favor: ', pf, '- Porcentaje en contra: ', pc)
