"""
Se pide un programa que le solicite al usuario que ingrese una palabra. con esa palabra calcular los siguientes puntos:
    - Determinar la cantidad de letras que tiene la palabra.
    - Mostrar un mensaje que informa si la palabra termina en vocal.
"""

palabra = input("Ingrese una palabra: ")
cantidad_letras = len(palabra)
if palabra[cantidad_letras - 1] == 'a' \
        or palabra[cantidad_letras - 1] == 'e' \
        or palabra[cantidad_letras - 1] == 'i' \
        or palabra[cantidad_letras - 1] == 'o' \
        or palabra[cantidad_letras - 1] == 'u':
    respuesta = "La palabra termina en vocal."
else:
    respuesta = "La palabra no termina en vocal."

print(cantidad_letras)
print(respuesta)
