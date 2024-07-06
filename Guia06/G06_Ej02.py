"""
Ingresar una serie de números por teclado que representan la cantidad de ventas realizadas en las diferentes sucursales
de un país de una determinada empresa.
Los requerimientos funcionales del programa son:
a) Informar la cantidad de ventas ingresadas.
b) Total de ventas.
c) Cantdidad de ventas cuyo valor este comprendido entre 100 y 300 unidades.
d) Indicar si hubo una cantidad de ventas inferior a 50 unidades.
Usted deberá ingresar cantidades de ventas hasta que se ingrese un valor negativo.
"""

# Se inicializan los contadores y acumuladores
contador = 0
acumulador = 0
contador_100_300 = 0
contador_especifico = 0
ventas_menor_50 = False

# Se le pide al usuario que ingrese una cantidad de ventas realizadas
ventas = int(input("Ingrese la cantidad de ventas realizadas: "))

# Mientras la cantiddd de ventas sea mayor o igual a 0(cero), procesamos los datos
while ventas >= 0:
    contador += 1
    acumulador += ventas

    # Si la cantidad de ventas está entre 100 y 300, se actualiza su contador
    if 100 <= ventas <= 300:
        contador_100_300 += 1
    # Si la cantidad de ventas es 400 o 500 o 600, se actualiza su contador
    if ventas == 400 or ventas == 500 or ventas == 600:
        contador_especifico += 1
    # Si las ventas ingresadas son menores a 50, actualizamos su contador
    if ventas < 50:
        ventas_menor_50 = True

    # Se vuelve a pedir que ingrese una catidad de ventas realizadas
    ventas = int(input("Ingrese la cantidad de ventas realizadas: "))

# Mostramos los resultados
print(f"La cantidad de ventas ingresadas fue {contador}")
print(f"El total de ventas fue {acumulador}")
print(f"La cantidad de ventas entre 100 y 300 es {contador_100_300}")
print(f"La cantidad de ventas con 400, 500 o 600 unidades es {contador_especifico}")

# Si hubieron ventas con menos de 50 unidades, lo informamos
if ventas == False:
    print("No hubo ventas menores a 50 unidades.")
else:
    print("Hubo al menos una venta menor a 50 unidades.")
