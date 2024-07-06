"""
Se ingresan las medidas de frente y fondo de un terreno.
Determinar si es cuadrado o rectangular y calcular su superficie
"""

frente = float(input("Ingresar la medida del frente del terreno: "))
fondo = float(input("Ingresar la medida del fondo del terreno: "))

if frente == fondo:
    forma_del_terreno = "cuadrado"
else:
    forma_del_terreno = "rectangular"

superficie = frente * fondo

print(f"El terreno es {forma_del_terreno} y su superficie es {superficie}.")


