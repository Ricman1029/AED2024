# n1 = int(input('Primer valor: '))
# n2 = int(input('Segundo valor: '))
#
# if n1 > n2:
#     may = n1
# else:
#     may = n1
#
# print('Mayor: ', may)

# __author__ = 'Cátedra de AED'
#
#
# import random
#
# # Titulo principal...
# print('Selección aleatoria de una carta de la baraja española...')
#
# # Seleccion del número de la carta...
# n = random.randint(1, 12)
#
# # Selección del palo de la carta...
# palos = 'Espada', 'Basto', 'Oro', 'Copa'
# p = random.choice(palos)
#
# # Visualización de resultados...
# print('La carta seleccionada es:')
# print('Palo:', p, '- Valor:', n)

# import random
#
# print('Ejemplo de uso de random.random()...')
# f = random.random()
# i = int(f * 10) + 1
# print('El valor generado es:', i)
#
import random
#
# i = 0
# billete = ()
# while i < 15:
#     billete = billete + (random.randint(0, 100), )
#     i += 1
#
# print(billete)

# billete = tuple(random.randint(0, 100) for _ in range(15))
# print(billete)
