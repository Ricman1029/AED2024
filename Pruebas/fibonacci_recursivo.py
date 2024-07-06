def fibonacci(numero):
    if numero == 0:
        return 0
    if numero == 1:
        return 1
    
    return fibonacci(numero - 1) + fibonacci(numero - 2)


numero = 1
while numero > 0:
    numero = int(input("Ingrese un numero: "))
    print(f"El {numero}º de la serie es: {fibonacci(numero)}")
