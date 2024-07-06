print("Este es un programa con varios usos. Siga las instrucciones.")

# Esto es una solución rápida a un problema
# Me sirve para que no se vuelva a llamar a main() al salir de main()
bandera = 0

# "Página" principal del programa
def main():
	while True:
		llamada = input("\nBienvenid@!"
						"\nEl código 'de' permite hacer divisiones enteras."
						"\nEl código 'bd' perimte convertir un número binario a decimal."
						"\nEl código 'od' perimte convertir un número binario a decimal."
						"\nEl código 'hd' perimte convertir un número binario a decimal."
						"\nEl código 'x' es para finalizar el programa."
						"\nIngrese el código que desee: ")

		if llamada == "de":
			division_entera()
		elif llamada == "bd":
			binario_decimal()
		elif llamada == "od":
			octal_decimal()
		elif llamada == "hd":
			hexa_decimal()
		elif llamada == "x":
			bandera = 1
			break
		else:
			print("El código ingresado (", llamada, ") no existe.\n")

	print("El programa a sido finalizado.\n")

# Devuelve el cociente y el resto de una division entera
def division_entera():
	print("\nIngrese dos números para ver el resultado de la división entera y su resto."
		  "\nIngrese 'x' para volver al inicio.")

	while ((num1 := input("Primer número: ")) != "x" and (num2 := input("Segundo número: ")) != "x"):
		print("Cociente:", int(num1) // int(num2), " - Resto:", int(num1) % int(num2))
		print()


# Convierte de número binario a número decimal
def binario_decimal():
	print("\nIngrese un número binario para convertirlo a decimal."
		  "\nIngrese 'x' para volver al inicio.")
	while (numero := input("Ingrese el numero: ")) != "x":
		# Sumamos todos los resultados de hacer: caracter * 2 ** indice para todos los caracteres de la numero, donde
		# "indice" es la posicion actual dentro de la numero (base 0 y contamos de derecha a izquierda)
		# "caracter" es el valor del caracter de la posición "indice"
		indice = len(numero) - 1
		suma = 0
	
		for caracter in numero:
			if caracter.isdigit():
				suma += int(caracter) * 2 ** indice
				indice -= 1
			else:
				print("¡EL CARACTER '", caracter, "'NO ES UN NÚMERO!")

		print("Número en decimal: ", suma)
		print()


def octal_decimal():
	print("\nIngrese un número octal para convertirlo a decimal."
		  "\nIngrese 'x' para volver al inicio.")
	while (numero := input("Ingrese el número octal: ")) != "x":
		indice = len(numero) - 1
		suma = 0

		for caracter in numero:
			if caracter.isdigit():
				suma += int(caracter) * 8 ** indice
				indice -= 1
			else:
				print("¡EL CARACTER '", caracter, "'NO ES UN NÚMERO!")

		print("Número en decimal: ", suma)
		print()


def hexa_decimal():
	print("\nIngrese un número hexadecimal para convertirlo a decimal."
		  "\nIngrese 'x' para volver al inicio.")
	while (numero := input("Ingrese el número hexadecimal: ")) != 'x':
		indice = len(numero) - 1
		suma = 0
		numero_mayusculas = numero.upper()

		for caracter in numero_mayusculas:
			if caracter.isdigit():
				suma += int(caracter) * 16 ** indice
			elif caracter == 'A':
				suma += 10 * 16 ** indice
			elif caracter == 'B':
				suma += 11 * 16 ** indice
			elif caracter == 'C':
				suma += 12 * 16 ** indice
			elif caracter == 'D':
				suma += 13 * 16 ** indice
			elif caracter == 'E':
				suma += 14 * 16 ** indice
			elif caracter == 'F':
				suma += 15 * 16 ** indice
			else:
				print("¡EL CARACTER '", caracter, "' NO ES VÁLIDO EN EL SISTEMA HEXADECIMAL!")

			indice -= 1

		print("Número decimal: ", suma)
		print()

# Cuando se inicia el programa, se llama a la función main
if bandera == 0:
	main()