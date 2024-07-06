"""
En este Desafio 02 se propone el desarrollo y prueba de un programa que implemente el cálculo de los valores de la
conocida Sucesión 3n + 1 o Sucesión de Collatz. Se parte de un número entero positivo n y se aplica en forma sucesiva
la siguiente relación numérica hasta llegar eventualmente al valor 1:
Por ejemplo, si partimos de n = 13 y aplicamos la relación sucesivamente sobre el último valor calculado, se genera la
siguiente secuencia hasta que finalmente se llega al 1: [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]. El conjunto de valores así
obtenidos, se suele designar como la órbita de n, y el número de iteraciones (que es el tamaño del conjunto de valores
obtenidos) hasta alcanzar el 1 partiendo desde n, se suele conocer como la longitud de la órbita de n o también como el
tiempo total de parada de n (o el total stopping time de n).

Su tarea es desarrollar un programa que permita cargar por teclado el valor de n, y luego calcule y muestre todos los
valores de la órbita de n, mostrando también (al final) el valor de la longitud de la órbita de n, el promedio entre
todos los valores de esa órbita, y el valor que haya sido el mayor de todos en la órbita. Por ejemplo, si se carga
n = 13, la salida del programa debería ser la siguiente:

n = 13

Orbita de n = 13 (valores calculados incluyendo al 13 y al 1): [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

Longitud de la órbita (cantidad de valores calculados hasta llegar al 1): 10

Promedio de todos los valores de la órbita: 11.9

Mayor de los números en esa órbita: 40
"""


# Generamos la suceción de Collatz con el número que ingresa el usuario
def sucesion_collatz(numero_inicial):
    orbita = numero_inicial,

    # Iniciamos la sucesión
    while numero_inicial != 1:
        if numero_inicial % 2 == 0:
            numero_inicial = numero_inicial // 2
        else:
            numero_inicial = 3 * numero_inicial + 1

        orbita += numero_inicial,

    return orbita


# Imprimimos toda la sucesión generada
def imprimir_orbita(numero_inicial, orbita):
    contador = 1
    largo_tupla = len(orbita)

    print(f"Orbita de n = {numero_inicial} (valores calculados incluyendo al {numero_inicial} y al 1): [", end="")

    for elemento in orbita:
        print(elemento, end="")
        if contador < largo_tupla:
            print(", ", end="")
        contador += 1

    print("]")


# Calculamos el promedio de la órbita
def promedio_orbita(orbita):
    suma_elementos = 0
    for elemento in orbita:
        suma_elementos += elemento

    return suma_elementos / len(orbita)


# Calculamos el mayor número de la órbita
def mayor_en_orbita(orbita):
    mayor = None
    for elemento in orbita:
        if mayor is None or elemento > mayor:
            mayor = elemento

    return mayor


# Le pedimos al usuario que ingrese un n entero positivo
n = -1
while n < 1:
    n = int(input("Ingrese un número entero positivo: "))
    if n < 1:
        print("Error. Se pide un número entero positivo.")

# Guardamos el resultado de la sucesión de Collatz en 'orbita_n'
orbita_n = sucesion_collatz(n)

# Imprimimos la orbita
imprimir_orbita(n, orbita_n)
# Mostramos la longitud de la orbita
print(f"Longitud de la órbita (cantidad de valores calculados hasta llegar al 1): {len(orbita_n)}")
# Calculamos el promedio de todos los valores de la orbita y lo mostramos
print(f"Promedio de todos los valores de la órbita:  {promedio_orbita(orbita_n)}")
# Mostramos el mayor de los números en la órbita
print(f"Mayor de los números en esa órbita:  {mayor_en_orbita(orbita_n)}")
