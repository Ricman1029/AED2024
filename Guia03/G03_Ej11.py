"""
Desarrollar un programa que permita ingresar una palabra por teclado y la devuelva enmascarada, mostrando la primer
letra y la última, pero reemplazando los caracteres itermedios por astericos.
Por ejemplo: si se ingresa la palabra "verde" se debe obtener "v***e"
"""

palabra = input("Ingrese una palabra que quiera enmascarar: ")
palabra_enmascarada = palabra[0] + '*' * (len(palabra) - 2) + palabra[len(palabra) - 1]

print(palabra_enmascarada)
