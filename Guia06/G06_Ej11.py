"""
Un matemático desea un simple programa que le permita cargar una serie de números que representan los discriminantes de
diferentes ecuaciones de segundo grado, el proceso de la secuencia finaliza cuando el matemático no desea seguir cargando
discriminantes. Usted debe:

a) Determinar la cantidad de discriminantes que darán 2 raíces.
b) Determinar la cantidad de discriminantes que darán una única raíz.
c) Determinar la cantidad de discriminantes que daran raíces en el campo de los números imaginarios.
d) Indicar el porcentaje que representa el punto c sobre el total de discriminantes procesados por el matemático.
"""

# Inicializamos las variables que vamos a utilizar
raices_reales = raices_imaginarias = una_raiz = 0

# Esta variable le da comienzo al bucle "while"
opcion = "s"

while opcion == "s":
    print("Ingrese los valores a, b y c de la discriminante: ")
    # Le pedimos al usuario que ingrese una discriminante
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))

    # Calculamos la discriminante
    discriminante = b ** 2 - 4 * a * c

    # Si la discriminante es mayor que 0, la ecuación va a tener 2 raíces reales
    if discriminante > 0:
        raices_reales += 1
    # Si la discriminante es menor que 0, la ecuación va a tener 2 raíces imaginarias
    elif discriminante < 0:
        raices_imaginarias += 1
    # Sino, la ecuación solo va a tener una raiz
    else:
        una_raiz += 1

    opcion = input("Desea seguir ingresando discriminantes? (s/n): ")

# Obtenemos el porcentaje de imaginarias respecto al total
total_discriminantes = raices_reales + raices_imaginarias + una_raiz
porcentaje_imaginarias = raices_imaginarias * 100 / total_discriminantes

# Mostramos los resultados
print(f"La cantidad de discriminantes que darán raíces reales son {raices_reales}")
print(f"La cantidad de discriminantes que darán raíces imaginarias son {raices_imaginarias}")
print(f"La cantidad de discriminantes que darán una sola raíz {una_raiz}")
print(f"El porcentaje de imaginarias respecto al total de discriminantes es {porcentaje_imaginarias}%")
