#	Mensaje de inicio
print('Este programa devuelve los dos últimos dígitos del número natural que ingrese el usuario.')

numero = int(input('Ingrese un número: '))
ultimo = numero % 10

numero2 = numero // 10
ultimo2 = numero2 % 10

print('El último dígito que ingresó es: ', ultimo)
print('Los últimos dos dígitos que ingresó son: ', ultimo2, ' y ', ultimo)