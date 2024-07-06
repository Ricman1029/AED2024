"""
Desarrollar un programa que permita procesar los datos del último censo de una pequeña población.
Por cada habitante se ingresa: sexo (M/F) y edad. La carga de datos finaliza al ingresar cualquier otro valor para sexo.
El programa debe informar:
a) A qué sexo corresponde la mayor cantidad de habitantes (considerar que puede ser igual)
b) Cantidad de mujeres en edad escolar (4 a 18 años inclusive)
c) Si hay algún varón que supere los 80 años de edad
"""

# Inicializamos las variables que vamos a utilizar
cantidad_Masculino = cantidad_Femenino = cantidad_Femenino_escolar = cantidad_total = 0
hombre_viejo = False

# Pedimios al usuario que ingrese el sexo de la persona
sexo_habitante = input("Ingrese el sexo (M/F): ")

# Si el sexo ingresado es válido, realizamos el resto de las operaciones
while sexo_habitante == "M" or sexo_habitante == "F":
    cantidad_total += 1

    # Pedimos al usuario que ingrese la edad de la persona
    edad_habitante = int(input("Ingrese la edad: "))

    # Vamos sumando las cantidades de hombres y mujeres en sus respectivas variables
    if sexo_habitante == "M":
        cantidad_Masculino += 1
        # Si es hombre y tiene mas de 80 años, actualizamos la variable
        if edad_habitante > 80:
            hombre_viejo = True
    else:
        cantidad_Femenino += 1
        # Si es mujer y tiene entre 4 y 18 años, actualizamos la variable necesaria
        if 4 <= edad_habitante <= 18:
            cantidad_Femenino_escolar += 1

    # Pedimos al usuario que ingrese el sexo de otra persona
    sexo_habitante = input("Ingrese el sexo (M/F): ")

# Determinamos a qué sexo corresponde la mayor cantidad de habitantes
if cantidad_Masculino == cantidad_Femenino:
    print("Hay la misma cantidad de hombres y mujeres.")
elif cantidad_Masculino > cantidad_Femenino:
    print("Hay mas hombres que mujeres.")
else:
    print("Hay mas mujeres que hombres.")

# Mostramos la cantidad de mujeres con edad escolar
print(f"Hay {cantidad_Femenino_escolar} mujeres en edad escolar.")

# Mostramos si hay algún varón que supere los 80 años
if hombre_viejo == True:
    print("Hay al menos un varón que supera los 80 años de edad.")
else:
    print("Ningún varón supera los 80 años de edad.")
