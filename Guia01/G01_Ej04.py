#	Mensaje de inicio
print('Este programa devuelve los dos últimos dígitos del número natural que ingrese el usuario.')

numero = int(input('Ingrese un número: '))

#	El operado módulo siempre devuelve un int
ultimoDigito = numero % 10
ultimosDosDigitos = numero % 100

''' 
	Este código tiene un problema y es que si el ante-último número ingresado es un 0
	la variable "ultimosDosDigitos" solo muestra el último dígito ya que el 0 a la izquierda 
	no tiene valor.
	Este problema no existe en la solución que implementé para el Ej04'.
'''
print('El último dígito que ingresó es: ', ultimoDigito)
print('Los últimos dos dígitos que ingresó son: ', ultimosDosDigitos)