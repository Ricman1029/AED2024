print("Ingresando dos números, te devuelve el resultado de la división entera con su resto.\nPara finalizar el programa ingresar 'f' cuando lo pida")


while ((num1 := input("Primer número: ")) != "f" and (num2 := input("Segundo número: ")) != "f"):
	print("Cociente:", int(num1) // int(num2), " - Resto:", int(num1) % int(num2))

print("Proceso finalizado")