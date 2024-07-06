"""
Escribir un programa, que le permita a un usuario a través de un menu de opciones, las siguiente operaciones:

  a) Ingresar el numero de CUIT de una persona (99-99999999-9) y determinar si el mismo el valido bajo las siguientes
  condiciones:

         1 - Contiene 13 caracteres, todos dígitos con dos guiones en la 3er y en la 11a posición

         2 - El dígito verificador es igual al ultimo dígito del CUIT, para obtener el dígito verificador se debe
         multiplicar cada uno de los 10 dígitos por la secuencia 5432765432 e ir acumulando el producto, luego se
         calcula el resto modulo 11 y por ultimo a 11 se le resta el resto del modulo obtenido. El resultado es el
         dígito verificador

  b) Ingresar el DNI de una persona y determinar si el mismo el valido (X9.999.999)

  c) Salir
"""


def validar_cuit(cadena):
    # Chequeamos que la cadena tenga 13 caracteres
    if len(cadena) != 13:
        return False

    posicion = 1
    suma_productos = 0
    for caracter in cadena:
        # Si no hay un guion en la posición 3 u 11, es inválido
        if posicion == 3 or posicion == 12:
            if caracter != "-":
                return False
        # Si los caracteres de las otras posiciones NO son dígitos, es inválido
        else:
            if not caracter.isdigit():
                return False
            # Vamos acumulando los productos del dígito con 5432765432 para obtener el dígito verificador
            suma_productos += int(caracter) * 5432765432

        posicion += 1

    # Obtenemos el dígito verificador
    resto_suma_prod = suma_productos % 11
    digito_verificador = 11 - resto_suma_prod

    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = 9

    if int(cadena[len(cadena) - 1]) != digito_verificador:
        return False

    return True


def validar_dni(cadena):
    if len(cadena) != 10:
        return False

    posicion = 1
    for caracter in cadena:
        if posicion == 3 or posicion == 7:
            if caracter != ".":
                return False
        else:
            if not caracter.isdigit():
                return False

        posicion += 1

    return True


menu = "1) Ingrese un CUIT \n" \
       "2) Ingrese un DNI \n" \
       "3) Salir \n" \
       "Elija una opción: "

opcion = -1
while opcion < 1 or opcion > 3:
    opcion = int(input(menu))
    if opcion < 1 or opcion > 3:
        print("Error. Se pide una elección entre 1 y 3.")

while opcion != 3:
    # Chequeamos el número de CUIT
    if opcion == 1:
        numero_cuit = input("Ingrese el número de CUIT: ")
        cuit_valido = validar_cuit(numero_cuit)
        if cuit_valido:
            print("El número de CUIT es válido.")
        else:
            print("El número de CUIT es inválido.")

    # Chequeamos el número de DNI
    elif opcion == 2:
        numero_dni = input("Ingrese el número de DNI: ")
        dni_valido = validar_dni(numero_dni)
        if dni_valido:
            print("El número de DNI es válido.")
        else:
            print("El número de DNI es inválido.")

    opcion = -1
    while opcion < 1 or opcion > 3:
        opcion = int(input(menu))
        if opcion < 1 or opcion > 3:
            print("Error. Se pide una elección entre 1 y 3.")
