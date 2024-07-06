"""
Según la Ley Electoral de la República Argentina, el Presidente y el Vicepresidente se eligen de acuerdo a las
siguiente reglas:

Artículo 149. - Resultará electa la fórmula que obtenga más del cuarenta y cinco por ciento (45%) de los votos
afirmativos válidamente emitidos y, además, existiere una diferencia mayor de diez puntos porcentuales respecto del
total de los votos afirmativos válidamente emitidos, sobre la fórmula que le sigue en número de votos.

Artículo 151. - En la segunda vuelta participarán solamente las dos fórmulas más votadas en la primera, resultando
electa la que obtenga mayor número de votos afirmativos válidamente emitidos.

Desarrllar un programa que permita ingresar, para los 3 partidos más votados: fórmula (presidente + vice) y cantidad de
votos obtenidos

Luego determinar:
    - Qué fórmula obtuvo el mayor porcentaje.
    - Si la fórmula resulta elegida o se requiere segunda vuelta. En este caso, indicar también quienes participan de
    la segunda vuelta.
"""

# # Carga de datos
# formula1 = input("Ingrese el candidato a presidente de la primer fórmula: "), \
#             input("Ingrese el candidato a vicepresidente de la primer fórmula: "), \
#             int(input("Ingrese la cantidad de votos obtenidos de la primer fórmula: "))
#
# formula2 = input("Ingrese el candidato a presidente de la segunda fórmula: "), \
#             input("Ingrese el candidato a vicepresidente de la segunda fórmula: "), \
#             int(input("Ingrese la cantidad de votos obtenidos de la segunda fórmula: "))
#
# formula3 = input("Ingrese el candidato a presidente de la tercer fórmula: "), \
#             input("Ingrese el candidato a vicepresidente de la tercer fórmula: "), \
#             int(input("Ingrese la cantidad de votos obtenidos de la tercer fórmula: "))
#
# # Procesamiento
# total_votos = formula1[2] + formula2[2] + formula3[2]
#
# # Porcentaje de votos para cada fórmula
# porcentaje1 = formula1[2] / total_votos
# porcentaje2 = formula2[2] / total_votos
# porcentaje3 = formula3[2] / total_votos
#
# # Fórmula con el mayor porcentaje y la del medio
# if porcentaje1 > porcentaje2 and porcentaje1 > porcentaje3:
#     mayor_porcentaje = porcentaje1
#     if porcentaje2 > porcentaje3:
#         medio_porcentaje = porcentaje2
#     else:
#         medio_porcentaje = porcentaje3
# elif porcentaje2 > porcentaje3:
#     mayor_porcentaje = porcentaje2
#     if porcentaje1 > porcentaje3:
#         medio_porcentaje = porcentaje1
#     else:
#         medio_porcentaje = porcentaje3
# else:
#     mayor_porcentaje = porcentaje3
#     if porcentaje1 > porcentaje2:
#         medio_porcentaje = porcentaje1
#     else:
#         medio_porcentaje = porcentaje2
#
# # Si el ganador de la primera vuelta gana con un porcentaje mayor 45% de los votos
# # Y la diferencia con el segundo es mayor a 10%, gana el primero y NO hay balotaje
# if mayor_porcentaje > 45 and mayor_porcentaje - medio_porcentaje > 10:
#     balotaje = False
# # Sino, hay balotaje
# else:
#     balotaje = True
#
# # Si hay balotaje, se vuelve a votar para las dos formulas ganadoras
# if balotaje:
# EN ESTE PUNTO ME DÍ CUENTA QUE PUEDO USAR SIEMPRE TUPLAS PARA FACILITAR EL PROCEDIMIENTO.
# AHORA LO REPIENSO PERO USANDO SIEMPRE TUPLAS

# Carga de datos
formula1 = input("Ingrese el candidato a presidente de la primer fórmula: "), \
            input("Ingrese el candidato a vicepresidente de la primer fórmula: "), \
            int(input("Ingrese la cantidad de votos obtenidos de la primer fórmula: "))

formula2 = input("Ingrese el candidato a presidente de la segunda fórmula: "), \
            input("Ingrese el candidato a vicepresidente de la segunda fórmula: "), \
            int(input("Ingrese la cantidad de votos obtenidos de la segunda fórmula: "))

formula3 = input("Ingrese el candidato a presidente de la tercer fórmula: "), \
            input("Ingrese el candidato a vicepresidente de la tercer fórmula: "), \
            int(input("Ingrese la cantidad de votos obtenidos de la tercer fórmula: "))

# Procesamiento
# Cantidad total de votos
total_votos = formula1[2] + formula2[2] + formula3[2]

# Porcentaje de votos para cada fórmula
formula1 += ((formula1[2] / total_votos * 100), )
formula2 += ((formula2[2] / total_votos * 100), )
formula3 += ((formula3[2] / total_votos * 100), )

# Ordenamos las fórmulas de mayor a menor en base al porcentaje de votos de manera que queden:
# formula1 = mayor, formula2 = medio, formula3 = menor
if not (formula1[3] >= formula2[3] >= formula3[3]):
    if formula1[3] < formula2[3]:
        formula1, formula2 = formula2, formula1
    if formula1[3] < formula3[3]:
        formula1, formula3 = formula3, formula1
    if formula2[3] < formula3[3]:
        formula2, formula3 = formula3, formula2

# Si el porcentaje de formula1 es mayor a 45 y la diferencia con el porcentaje de formula2 es mayor a 10
# No hay balotaje y gana la formula1
# También anunciamos si hay o no balotaje
if formula1[3] > 45 and formula1[3] - formula2[3] > 10:
    balotaje = False
    # Mostramos la fórmula ganadora
    print(f"La fórmula que obtuvo el mayor porcentaje fue la formula del presidente {formula1[0]} y el vice {formula1[1]}.")
    print("No se requiere balotaje.")
else:
    balotaje = True
    print("Hay balotaje.")
    print(f"Participan del balotaje la fórmula del candidato {formula1[0]} y la fórmula del candidato {formula2[0]}")

# Si hay balotaje, se vuelven a realizar los votos para las primeras dos formulas
if balotaje:
    formula1 = formula1[0], formula1[1], \
        int(input("Ingrese la cantidad de votos para la primer formula: "))
    formula2 = formula2[0], formula2[1], \
        int(input("Ingrese la cantidad de votos para la segudna formula: "))

    # Cantidad total de votos
    total_votos = formula1[2] + formula2[2]

    # Porcentaje de votos para cada fórmula
    formula1 += ((formula1[2] / total_votos * 100),)
    formula2 += ((formula2[2] / total_votos * 100),)

    # Ordenamos las fórmulas de mayor a menor en base al porcentaje de votos
    if formula1[3] < formula2[3]:
        formula1, formula2 = formula2, formula1

    # Anunciamos al ganador de las elecciones
    print(f"La fórmula que obtuvo el mayor porcentaje fue la formula del presidente {formula1[0]} y el vice {formula1[1]}.")
