"""
La empresa de peajes AED Pase-Pase S.R.L, festeja su séptimo aniversario y, por tal motivo, el día de hoy ofrece premios
a sus clientes.
Estos premios se calculan de la siguiente manera:
    1) Cada vez que pasa un cleinte, se sortea un número del 0 al 9. Si el número coincide con el último dígito de la
    patente del vehículo, se le cobra la tarifa promocional de $50, sino, se le cobra la tarifa estándar de $90.
    2) Independientemente de la tarifa que deba pagar, si el último dígito de la patente es 7, entonces recibe un
    descuento del 50%, en caso contrario un descuento del 10%
Desarrolle un programa en Python que le solicite al usuario los dígitos de su patente (únicamente los dígitos), simule
su paso por el peaje e indique el monto a abonar.
"""
import random

numero_random = random.randint(0, 9)

digitos_patente = input("Ingrese los digitos de su patente: ")
ultiimo_digito_patente = digitos_patente[len(digitos_patente) - 1]

if ultiimo_digito_patente == str(numero_random):
    tarifa = 50
else:
    tarifa = 90

if ultiimo_digito_patente == '7':
    descuento = 50
else:
    descuento = 10

tarifa_final = tarifa * ((100 - descuento) / 100)

print(tarifa_final)
