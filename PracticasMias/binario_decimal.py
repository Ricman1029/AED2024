print("Ingresar secuencia de ceros (0) y unos (1) para convertirlo a decimal\nPresione la letra 'f' para finalizar el procedimiento.")

while (secuencia := input("Ingrese la secuencia: ")) != "f":
	indice = len(secuencia) - 1
	suma = 0
	
	for caracter in secuencia:
		suma += int(caracter) * 2 ** indice
		indice -= 1

	print("Número en decimal: ", suma)

print("Proceso finalizado")