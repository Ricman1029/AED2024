"""
Se pide desarrollar un programa que permita leer una serie de números. La finalización de carga de datos se presenta
cuando el usuario ingrese un número negativo.
Los requerimientos funcionales del programa son:
a) La sumatoria de solo los números que estén comprendidos entre 50 y 100.
b) Cantidad de valores pares ingresados.
c) CAntidad de valores impares ingresados.
d) Informar si en la carga de números se ingreso al menos un número 0.
e) Informar si la serie contiene solo números pares e impares alternados
"""

# Inicializamos las variables que vamos a utilizar
suma = pares = impares = contador = 0
cero = False
alternado = True

# Pedimos al usuario que ingrese un número.
numero = int(input("Ingrese un número (si es menor a 0 se termina): "))

# Si el primer número ingresado es par, vamos a chequear que en todos los contadores par, el número ingresado sea par.
# Sino, hacemos al véres
if numero % 2 == 0:
    empieza = "par"
else:
    empieza = "impar"

while numero >= 0:
    # Sumamos todos los números comprendidos entre 50 y 100
    if 50 <= numero <= 100:
        suma += numero

    # Obtenemos la cantidad de números pares e impares ingrsados
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    # Si se ingresó un número 0(cero) lo informamos
    if numero == 0:
        cero = True

    # Si la serie contiene solo números pares e impares alternados, lo informamos
    if empieza == "impar":
        if contador % 2 == 0 and numero % 2 == 0 or contador % 2 != 0 and numero % 2 != 0:
            alternado = False
    else:
        if contador % 2 == 0 and numero % 2 != 0 or contador % 2 != 0 and numero % 2 == 0:
            alternado = False

    # Pedimos al usuario que ingrese un nuevo número, y actualizamos contador
    numero = int(input("Ingrese un número (si es menor a 0 se termina): "))
    contador += 1

# Mostramos los resultados
print(f"La suma de todos los números entre 50 y 100 es {suma}.")
print(f"Se ingresaron {pares} números pares.")
print(f"Se ingresaron {impares} números impares.")

# Nos fijamos si se ingreso al menos un valor igual a 0(cero) y lo informamos
if cero == True:
    print("Se ingresó al menos un valor igual a 0(cero).")
else:
    print("No se ingresó ningún valor igual a 0(cero).")

# Nos fijamos si la serie solo contiene números pares e impares alternados y lo informamos
if alternado == True:
    print("La serie solo contiene números pares e impares alternados.")
else:
    print("Los números pares e impares de la serie no estan alternados.")