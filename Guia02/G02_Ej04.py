#   Mensaje de inicio
print('Este programa calcula el valor de un polinomio de grado 2 en un punto x dado, y sus raíces.')

a = float(input('Ingrese el coeficiente principal del polinomio: '))
b = float(input('Ingrese el coeficiente lineal del polinomio: '))
c = float(input('Ingrese la ordenada al origen del polinomio: '))
x = float(input('Ingrese el punto x para el cual quiere saber el valor del polinomio: '))

raiz1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
raiz2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
punto = a*x**2 + b*x + c

print('Las raices del polinomio son : ', raiz1, 'y', raiz2)
print('El polinomio en el punto x dado vale: ', punto)

#   (x + 3)(x + 2)