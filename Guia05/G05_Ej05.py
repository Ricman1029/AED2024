"""
Diseñar un programa que según la opción ingresada por el usuario permita realizar las siguientes operaciones:
    - Si la opción es 1 mostrar la superficie de un triángulo. Para calcular la superficie debe usarse la fórmula de Herón
    - Si la opción ingresada es 2 mostrar el perímetro del triángulo.
    - Si la opción ingresada es 3 informar la longitud del lado menor.
    - Si la opción ingresada no fue ni 1, 2 o 3 informar un mensaje de error.
Para ello usted deberá ingresar por teclado el número de opción y el valor de los tres lados del triángulo.
"""

opcion = int(input("Ingrese una opción (1- Superficie, 2- Perímetro, 3- Lado menor): "))

if opcion == 1 or opcion == 2 or opcion == 3:
    lado1 = int(input("Ingresar el lado 1: "))
    lado2 = int(input("Ingresar el lado 2: "))
    lado3 = int(input("Ingresar el lado 3: "))

    if opcion == 1:
        s = (lado1 + lado2 + lado3) / 2
        superficie = (s * (s - lado1) * (s - lado2) * (s - lado3)) ** 0.5
        print(f"La superficie del triángulo es {superficie}")
    elif opcion == 2:
        perimetro = lado1 + lado2 + lado3
        print(f"La superficie del triángulo es {perimetro}")
    else:
        if lado1 > lado2:
            lado1, lado2 = lado2, lado1
        if lado1 > lado3:
            lado1, lado3 = lado3, lado1
        print(f"La longitud del menor de los 3 lados es {lado1}")
else:
    print(f"Error. La opcíon seleccionada ({opcion}) no es válida.")

