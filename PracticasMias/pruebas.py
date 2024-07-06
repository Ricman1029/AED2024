import time
import os

MAX = 10

contador = 0
while True:
    numero = int(input("Ingrese un número: "))
    
    if contador + numero > MAX:
        contador = numero - (MAX - contador)
    else:
        contador += numero
    
    os.system("cls")
    print(contador)
    