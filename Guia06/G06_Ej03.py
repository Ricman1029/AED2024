"""
Realice un programa que le ofrezca al usuario un menú de opciones que le permita ejecutar las siguientes acciones:
Opción 1: Calcular promedio de 1000 números aleatorios generados en el rango [0, 100000]
Opción 2: Buscar el mayor de 10000 números aleatorios generados en el rango de [0, 100000]
Opción 3: buscar el menor de 5000 números aleatorios generados en el rango de [0, 100000] y calcular el valor promedio
de los números menores a 10000
Cualquier otro número: Salir del programa
"""
import random

# Se inicializa el contador y el promedio
contador = 0

# Se le pide al usuario que elija una opción
opcion = int(input("Ingrese una opción (1, 2, 3): "))

# Se analiza la opción para saber qué hacer
if opcion == 1:
    print("El programa calcula el promedio de 1.000 números aleatorios generados entre [0, 100000]")

    # Se inicializa el acumulador
    acumulador = 0

    while contador < 1000:
        # Se genera un número aleatorio entre 0 y 100.000
        aleatorio = random.randint(0, 100000)
        contador += 1

        # Se calcula el promedio
        acumulador += aleatorio

    # Se calcula el promedio
    promedio = acumulador / contador

    # Mostramos el resultado
    print(f"El promedio de los 1000 números generados fue {promedio}")

elif opcion == 2:
    print("El programa busca el mayor de 10000 números aleatorios generados entre [0, 100000]")

    # Generamos un número aleatorio y actualizamos al contador
    aleatorio = random.randint(0, 100000)
    contador += 1
    # Como este es el único número, es el mayor de todos por ahora
    mayor = aleatorio

    while contador < 10000:
        # Si el mayor es menor que el número generado, lo igualamos al mismo
        if mayor < aleatorio:
            mayor = aleatorio

        # Generamos un nuevo número y actualizamos contador
        aleatorio = random.randint(0, 100000)
        contador += 1

    # Mostramos el resultado
    print(f"El mayor de los 10000 números generados fue {mayor}.")

elif opcion == 3:
    print("El programa busca el menor de 5.000 números aleatorios entre [0, 100000] y calcula el valor promedio "
          "de los números menores a 10000")

    # Inicializamos la variable que acumula todos los números generados menores a 10.000
    acumulador = 0

    # Generamos un número aleatorio y actualizamos el contador
    aleatorio = random.randint(0, 100000)
    contador += 1
    # Como este es el único número, es el menor de todos por ahora
    menor = aleatorio

    while contador < 5000:
        # Si el menor es mayor que el número generado, lo igualamos al mismo
        if menor > aleatorio:
            menor = aleatorio

        # Si el número generado es menor a 10.000, lo acumulamos para calcular el promedio después
        if aleatorio < 10000:
            acumulador += aleatorio

        # Generamos un número y actualizamos contador
        aleatorio = random.randint(0, 100000)
        contador += 1

    # Calculamos el promedio de los números menores a 10.000
    promedio = acumulador / contador

    # Mostramos los resultados
    print(f"El menor número de los 5000 generados fue {menor}")
    print(f"El promedio de los números menores a 10000 fue {promedio}")

# Si el número ingresado no es un número válido, el programa finaliza
else:
    print("El número ingresado es inválido. El programa finalizará.")
