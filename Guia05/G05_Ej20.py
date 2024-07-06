"""
Para calcular el premio de un vendedor, se ingresan 3 montos correspondientes a sus ventas mensuales del último
trimestre.
El premio es equivalente al 50% del menor monto vendido. Si además los montos superan los $1000, se agrega un 10%
adicional al premio calculado.

(*) Ejercicio tipo parcial
"""

# Se ingresan 3 montos correspondientes a sus ventas mensuales del último trimestre
monto1 = int(input("Ingrese el primer monto de las ventas mensuales: "))
monto2 = int(input("Ingrese el segundo monto de las ventas mensuales: "))
monto3 = int(input("Ingrese el tercer monto de las ventas mensuales: "))

# Calculamos el menor monto
menor = monto1
if menor > monto2:
    menor = monto2
if menor > monto3:
    menor = monto3

# El premio equivale al 50% del menor monto
premio = menor * .5

# Si los montos superan los $1000, se agrega un 10% adicional al premio calculado
if monto1 > 1000 or monto2 > 1000 or monto3 > 1000:
    premio *= 1.1

print(f"El premio del vendedor es ${premio}.")
