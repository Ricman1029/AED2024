"""
Una empresa debe calcular el total de comisiones que debe abonar por ventas realizadasa por sus vendedores, para ello le
solicita un sistemita que le permita calcular dichos montos.
Se tiene conocimiento que la empresa tiene cuatro categorías de vendedores (1 a 4). Usted debe solicitar el ingreso de
la categoría del vendedor y el total de la venta (el proceso termina cuando se ingrese una categoría igual a cero) y
acumular las comisiones de las ventas rendidas por los vendedores de diferentes en base a los siguientes cálculos:
a) Categoría 1: cobra una comisión de 10%
b) Categoría 2: cobra una comisión de 25%
c) Categoría 3: cobra una comisión de 30%
d) Categoría 4: cobra una comisión de 40%
Una vez procesadas todas las ventas mostrar el total de comisiones a pagar por cada categoría de vendedores que tiene la
empresa junto con el total general.
"""

# Inicializamos las variables que vamos a utilizar
comision1 = comision2 = comision3 = comision4 = 0

# Pedimos al usuario que ingrese la categoria del vendedor
categoria = int(input("Ingrese la categoría del vendedor: "))

while categoria != 0:
    total_venta = int(input("Ingrese el total de venta: "))

    # Vamos acumulando las comisiones de acuerdo a la categoría ingresada
    if categoria == 1:
        comision1 += total_venta * .10
    elif categoria == 2:
        comision2 += total_venta * .25
    elif categoria == 3:
        comision3 += total_venta * .30
    elif categoria == 4:
        comision4 += total_venta * .40

    # Pedimos al usuario que ingrese nuevamente la categoría
    categoria = int(input("Ingrese la categoría del vendedor: "))

# Calculamos la comision total general
comision_total = comision1 + comision2 + comision3 + comision4

# Informamos el total de comision de cada categoría y el total general
print(f"Se debe pagar por la categoría 1 ${comision1}")
print(f"Se debe pagar por la categoría 2 ${comision2}")
print(f"Se debe pagar por la categoría 3 ${comision3}")
print(f"Se debe pagar por la categoría 4 ${comision4}")
print(f"El total general a pagar es de ${comision_total}")
