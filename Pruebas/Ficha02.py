# __author__ = 'Cátedra AED'


# EJEMPLO 2
# # título general y carga de datos...
# print('Ejemplo 2 - Cálculo del sueldo de un empleado')
# nom = input('Ingrese el nombre del empleado: ')
# horas = int(input('Ingrese la cantidad de horas trabajadas: '))
# monto = float(input('Ingrese el monto a cobrar por hora: '))
#
# # procesos...
# sueldo = horas * monto
#
# # visualización de resultados...
# print('Empleado: ', nom, '- Sueldo a cobrar:', sueldo, 'pesos')


# EJEMPLO 3
# # título general y carga de datos...
# print('Ejemplo aritmética modular')
# print('Este programa expresa la cantidad de segundos ingresada en horas, minutos y segundos')
# segIn = int(input('Ingrese la cantidad de segundos que desea calcular: '))
#
# # procesos...
# horas = segIn // 3600
# segSobr = segIn % 3600
# min = segSobr // 60
# segFin = segSobr % 60
#
# # resultados...
# print(segIn, 'segundos equivalen a: ', horas, 'horas, ', min, 'minutos, y ', segFin, 'segundos.')


# n = input('Ingrese su nombre: ')
# print('El nombre ingresado es: ', n)
# n = int(input('Ahora ingrese su número de legajo: '))
# print('El legajo ingresado es: ', n)
# n = float( input('Y ahora ingrese su promedio: ') )
# print('El promedio ingresado es: ', n)

# __author__ = 'Catedra de Algoritmos y Estructuras de Datos'
#
# # inicialización de contadores, acumuladores y banderas...
# c1, c2, c3, t = 0, 0, 0, 0
# ok = False
#
# # proceso de carga por doble lectura...
#
# while cant != -1:
#
#     # punto a): chequear en qué intervalo está cada cantidad y contar...
#     if 0 <= cant < 10000:
#         c1 += 1
#     elif 10000 <= cant < 15000:
#         c2 += 1
#     else:
#         c3 += 1
#
#     # punto b): acumular cada cantidad...
#     t += cant
#
#     # punto c): chequear si cant es 0, y marcar con un flag...
#     if cant == 0:
#         ok = True
#
#     # hacer la segunda lectura...
#     cant = int(input('Ingrese otra cantidad (con -1 termina): '))
#
# # visualización de resultados... punto a)
# print()
# print('Cantidad de valores >= 0 pero < 10000:', c1)
# print('Cantidad de valores >= 10000 pero < 15000:', c2)
# print('Cantidad de valores >= 15000:', c3)
#
# # visualización de resultados... punto b)
# print('Cantidad total de vehículos vendidos:', t)
#
# # visualización de resultados... punto c)
# # recuerde que lo que sigue es equivalente a if ok == True:
# if ok:
#  print('Se registró al menos una cantidad de ventas igual cero')
# else:
#  print('No se registró ninguna cantidad de ventas igual cero')

