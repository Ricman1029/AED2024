"""
Una empresa nos solicitó un programa que nos permita calcular los precios de los productos que vende al publico. Para
ello, nuestro programa debe pedir el precio unitario, la cantidad que se vendió y si se pagó en efectivo o no.
En base a esto determinar_
    1) El precio final sin descuentos del artículo (precio unitario por cantidad)
    2) Calcular un descuento: Si el usuario pago en efectivo y la cantidad vendida es superior a 10 unidades del 15%;
    caso contrario solo aplicar un 5% de descuento.
"""

precio_unitario = float(input("Ingrese el precio unitario: "))
cantidad = int(input("Ingrese la cantidad que se vendió: "))
forma_pago = int(input("Ingrese '1' si pagó en efectivo, o '0' si no lo hizo: "))

precio_final_sin_descuento = precio_unitario * cantidad

if forma_pago and cantidad > 10:
    precio_final = precio_final_sin_descuento * .85
else:
    precio_final = precio_final_sin_descuento * .95

print(precio_final)
