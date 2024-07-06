# __author__ = 'Catedra de AED'
#
#
# def calcular(a, b):
#     if b != 0:
#         c = a // b
#         r = a % b
#         return c, r
#
# # script principal
# a, b = calcular(3, 0)
# print('Cociente:', a, 'Resto:', b)


# __author__ = 'Cátedra de AED'
#
#
# def comprobar(n1, n2):
#     if n1 > n2:
#         return n1
#
#
# def test():
#     n1 = int(input('Ingrese un número: '))
#     n2 = int(input('Ingrese otro: '))
#     r = comprobar(n1, n2)
#     print('El mayor es:', r)
#
#
# # script principal
# test()

# __author__ = 'Cátedra de AED'
#
#
# def mostrar(n):
#     if n < 0:
#         return
#     print('El número', n, 'es válido')
#
#
# def test():
#     n = int(input('Ingrese un número: '))
#     mostrar(n)
#     print('Programa terminado...')
#
#
# # script principal
# test()


# __author__ = 'Catedra de AED'
#
# import random
#
#
# def play_secret_number_game(limite_derecho, cantidad_intentos):
#
#     # limites iniciales del intervalo de búsqueda...
#     izq, der = 1, limite_derecho
#
#     # contador de intentos...
#     intentos = 0
#
#     # el numero secreto...
#     secreto = random.randint(1, limite_derecho)
#
#     # el ciclo principal... siga mientras no
#     # haya sido encontrado el número, y la
#     # cantidad de intentos no llegue a 5...
#     while intentos < cantidad_intentos:
#         intentos += 1
#         print('\nEl numero está entre', izq, 'y', der)
#
#         # un valor para forzar al ciclo a ser [1, N]...
#         num = izq - 1
#
#         # carga y validación del número sugerido por el usuario...
#         while num < izq or num > der:
#             num = int(input('[Intento: ' + str(intentos) + '] => Ingrese su numero: '))
#             if num < izq or num > der:
#                 print('Error... le dije entre', izq, 'y', der, '...')
#
#         # controlar si num es correcto, avisar y cortar el ciclo...
#         if num == secreto:
#             print('\nGenio!!! Acertaste en', intentos, 'intentos')
#             return
#
#         # ... pero si no lo es, ajustar los límites
#         # del intervalo de búsqueda... y seguir...
#         elif num > secreto:
#             der = num
#         else:
#             izq = num
#
#     print('\nLo siento!!! Se te acabaron los intentos. El número era:', secreto)
#
#
# def test():
#     print('Juego del Número Secreto... Configuración Inicial...')
#     ld = int(input('El número secreto estará entre 1 y: '))
#     ci = int(input('Cantidad máxima de intentos que tendrá disponible: '))
#     play_secret_number_game(ld, ci)
#
#
# # script principal...
# test()


__author__ = 'Catedra de AED'


def ejemplo():
    i = int(input('Ingrese un valor: '))
    t = int(input('Ingrese otro: '))
    if i > 3*t:
        ok = True

    if ok:
        print('El primer valor es mayor al triple del segundo...')


# script principal
ejemplo()