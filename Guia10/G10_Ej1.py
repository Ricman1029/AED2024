"""
Desarrollar un programa en Python que permita cargar por teclado un texto completo (analizar dos opciones: una es cargar
todo el texto en una variable de tipo cadena de caracteres y recorrerla con un for iterador; y la otra es cargar cada
caracter uno por uno a través de un while). Siempre se supone que el usuario cargará un punto para indicar el final del
texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco. El programa debe:

a) Determinar cuántas palabras tenían más de 4 letras.

b) Determinar cuántas palabras tenían al menos una vez la letra "x" o la letra "y".

c) Determinar el promedio de letras por palabra en todo el texto.

d) Determinar cuántas palabras contuvieron sólo una vez la expresión "mo".

********************************************************************************
Ejemplo: 'el mono momoxy toca el xilofon.'
********************************************************************************
Palabras con más de 4 letras: 2
Palabras tenían al menos una vez la letra "x" o la letra "y": 2
El promedio de letras por palabra en todo el texto es: 4.17
Determinar cuántas palabras contuvieron sólo una vez la expresión "mo": 1
"""

# Inicializamos variables
cont_letras = cont_mas_4_letras = cont_palabras = cont_pal_x_y = cont_letras_total = cont_pal_mo = cont_mo = 0
palabra_x_y = bandera_m = False

# Ingresar texto
cadena = input("Ingrese el texto: ")

for caracter in cadena:
    # Si el caracter es un espacio o un punto, quiere decir que terminamos de procesar la palabra anterior
    if caracter == " " or caracter == ".":
        # Agregamos una palabra al contador
        cont_palabras += 1

        # Si la palabra tiene mas de cuatro letras, actualizamos su contador
        if cont_letras > 4:
            cont_mas_4_letras += 1

        # Si la palabra tenía una x o una y, actualizamos su contador
        if palabra_x_y:
            cont_pal_x_y += 1
            palabra_x_y = False

        # Si la palabra tiene 'mo', lo contamos
        if cont_mo == 1:
            cont_pal_mo += 1

        # Reseteamos el contador de 'mo'
        cont_mo = 0

        # Agregamos la cantidad de letras al total de letras
        cont_letras_total += cont_letras
        cont_letras = 0

    # Estamos adentro de una palabra, hay que procesar la info
    else:
        # Contamos la cantidad de letras
        cont_letras += 1

        # Nos fijamos si la palabra contiene una 'x' o una 'y'
        if caracter == "x" or caracter == "y":
            palabra_x_y = True

        # Nos fijamos si la palabra tiene una 'm'
        if caracter == "m":
            bandera_m = True
        # Nos fijamos si la palabra tiene 'mo'
        else:
            if bandera_m and caracter == "o":
                cont_mo += 1
            bandera_m = False

promedio = cont_letras_total / cont_palabras

print(f"Palabras con más de 4 letras: {cont_mas_4_letras}")
print(f"Palabras tenían al menos una vez la letra 'x' o la letra 'y': {cont_pal_x_y}")
print(f"El promedio de letras por palabra en todo el texto es: {promedio}")
print(f"Determinar cuántas palabras contuvieron sólo una vez la expresón 'mo': {cont_pal_mo}")

