"""
Escribir un programa que le permita al usuario, a través de un menú de opciones, las siguientes operaciones:

a) Dada la serie de números naturales desde 1 hasta n (n ingresado por teclado y validando que sea mayor a cero) mostrar
la suma de los cuadrados

b) Ingresar un texto finalizado por un punto y determinar la cantidad de palabras que finalizan con vocales

c) Ingresar una serie de números (la carga finaliza con cero) y determinar si hay mayor cantidad de valores pares o de
impares

d) Salir
"""

print("1. Suma de los cuadrados de los números naturales desde 1 hasta n.")
print("2. Cantidad de palabras finalizadas por vocales dentro de un texto finalizado por un punto.")
print("3. Determinar si hay mas números pares o impares dentro de una serie de números.")
print("4. Salir.")
opcion = int(input("Ingrese una opción: "))

while opcion != 4:
    if opcion == 1:
        print("Se calculará la suma de los cuadrados de los números naturales entre 1 y n.")
        n = 0
        suma = 0
        while n <= 0:
            n = int(input("Ingrese n: "))
            if n <= 0:
                print("El número debe ser un número natural.")

        for i in range(1, n + 1):
            suma += i ** 2

        print(f"La suma de los cuadrados de los números naturales entre 1 y {n} es: {suma}")

    if opcion == 2:
        print("Se contarán la cantidad de palabras que terminan en vocal dentro de un texto finalizado en punto.")
        texto = input("Ingrese el texto finalizado por un punto: \n")
        largo_texto = len(texto)
        cont_palabras_terminan_vocal = 0

        # Suponemos que el texto finaliza con un punto
        """
        ESTE ERA MI CÓDIGO, EL PROFE USÓ UNO MEJOR
        for c in range(largo_texto - 1):
            caracter_act = texto[c]
            caracter_sig = texto[c + 1]

            # Primero chequéo que el siguiente caracter NO sea una letra
            # Después chequéo que el caracter actual sea una vocal
            if ("z" < caracter_sig or caracter_sig < "a" and "Z" < caracter_sig or caracter_sig < "A") and \
                    (caracter_act == "a" or caracter_act == "e" or caracter_act == "i" or caracter_act == "o" or
                     caracter_act == "u" or caracter_act == "A" or caracter_act == "E" or caracter_act == "I" or
                     caracter_act == "O" or caracter_act == "U"):
                cont_palabras_terminan_vocal += 1
        """
        """
        # CÓDIGO DEL PROFE
        # No funciona bien, ya que si hay un caracter no alfabético y distinto de espacio o punto, no es contado como
        # una palabra que termina en vocal por más que asi lo sea.
        caracter_anterior = " "
        vocales = "aeiouAEIOU"
        for caracter in texto:
            if caracter == ' ' or caracter == '.':
                if caracter_anterior in vocales:
                    cont_palabras_terminan_vocal += 1
            caracter_anterior = caracter
        """
        # Mi mejora sobre el código del profe
        caracter_anterior = " "
        vocales = "aeiouAEIOU"
        alfabeto = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        for caracter in texto:
            if caracter not in alfabeto:
                if caracter_anterior in vocales:
                    cont_palabras_terminan_vocal += 1
            caracter_anterior = caracter
        print(f"La cantidad de palabras que terminan en vocal es: {cont_palabras_terminan_vocal}")

    if opcion == 3:
        print("Se determinará si existen mas números pares o impares dentro de una serie de números distintos de cero.")
        numero = int(input("Ingrese un número (con cero termina): "))
        cont_pares = cont_impares = 0

        while numero != 0:
            if numero % 2 == 0:
                cont_pares += 1
            else:
                cont_impares += 1

            numero = int(input("Ingrese un número (con cero termina): "))

        if cont_pares > cont_impares:
            print("Hay mas números pares que impares.")
        elif cont_impares > cont_pares:
            print("Hay mas números impares que pares.")
        else:
            print("Hay tantos pares como impares.")

    print("1. Suma de los cuadrados de los números naturales desde 1 hasta n.")
    print("2. Cantidad de palabras finalizadas por vocales dentro de un texto finalizado por un punto.")
    print("3. Determinar si hay mas números pares o impares dentro de una serie de números.")
    print("4. Salir.")
    opcion = int(input("Ingrese una opción: "))

print("Se ingresó la opción 4. El programa finalizará.")
