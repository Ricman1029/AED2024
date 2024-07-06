"""
Una institución educativa necesita un programa que facilite la gestión de cupos de los cursos de primer grado. Ingresar
tres grados. De cada grado se ingresa el código de identificación (Ejemplo 1A, 1B, ...) y la cantidad de niños y de
niñas y cupo máximo (que es el mismo para los tres cursos).
Los requerimientos funcionales son:
    a) Código de idenitificación del curso que tenga menos alumnos inscriptos.
    b) Porcentaje de niñas de cada curso.
    c) Porcentaje de niños de cada curso.
    d) Promedio general de alumnos.
    e) Si algunos de los tres grados supera el cupo máximo informar un mensaje la necesidad de apertura de una nueva
    división.
"""


# Carga de datos
grado1 = input("Ingrese el código de ID: "), int(input("Ingrese la cantidad de niños: ")), \
    int(input("Ingrese la cantidad de niñas: "))
grado2 = input("Ingrese el código de ID: "), int(input("Ingrese la cantidad de niños: ")), \
    int(input("Ingrese la cantidad de niñas: "))
grado3 = input("Ingrese el código de ID: "), int(input("Ingrese la cantidad de niños: ")), \
    int(input("Ingrese la cantidad de niñas: "))
cupo_maximo = int(input("Ingrese el cupo máximo de alumnos: "))

# Procesos
codigo_ID, cantidad_niños, cantidad_niñas, cantidad_alumnos = 0, 1, 2, 3

# Se calcula la cantidad de alumnos totales en cada grado y se agrega como elemento de las tupla
grado1 += grado1[cantidad_niños] + grado1[cantidad_niñas],
grado2 += grado2[cantidad_niños] + grado2[cantidad_niñas],
grado3 += grado3[cantidad_niños] + grado3[cantidad_niñas],

# Se obtiene el grado con la menor cantidad de alumnos
if grado1[cantidad_alumnos] < grado2[cantidad_alumnos] < grado3[cantidad_alumnos]:
    menos_alumnos = grado1
elif grado2[cantidad_alumnos] < grado3[cantidad_alumnos]:
    menos_alumnos = grado2
else:
    menos_alumnos = grado3

# Se calcula el porcentaje de niñas en cada grado
porcentaje_niñas1 = round(grado1[cantidad_niñas] * 100 / grado1[cantidad_alumnos], 2)
porcentaje_niñas2 = round(grado2[cantidad_niñas] * 100 / grado2[cantidad_alumnos], 2)
porcentaje_niñas3 = round(grado3[cantidad_niñas] * 100 / grado3[cantidad_alumnos], 2)

# Se calcula el porcentaje de niños en cada grado
porcentaje_niños1 = round(grado1[cantidad_niños] * 100 / grado1[cantidad_alumnos], 2)
porcentaje_niños2 = round(grado2[cantidad_niños] * 100 / grado2[cantidad_alumnos], 2)
porcentaje_niños3 = round(grado3[cantidad_niños] * 100 / grado3[cantidad_alumnos], 2)

# Se calcula el promedio de la cantidad de alumnos en cada grado
promedio_alumnos = round((grado1[cantidad_alumnos] + grado2[cantidad_alumnos] + grado3[cantidad_alumnos]) / 3, 2)

# Muestra de datos
print(f"El grado con menos alumnos es {menos_alumnos[codigo_ID]}.")
print(f"El porcentaje de niñas en los grados {grado1[codigo_ID]}, {grado2[codigo_ID]}, {grado3[codigo_ID]} son \n"
      f"{porcentaje_niñas1}%, {porcentaje_niñas2}%, {porcentaje_niñas3}% respectivamente.")
print(f"El porcentaje de niños en los grados {grado1[codigo_ID]}, {grado2[codigo_ID]}, {grado3[codigo_ID]} son \n"
      f"{porcentaje_niños1}%, {porcentaje_niños2}%, {porcentaje_niños3}% respectivamente.")
print(f"El promedio de alumnos en los cursos es {promedio_alumnos}.")

# Abrir una nueva división si algun grado tiene mas alumnos que los permitidos
if (grado1[cantidad_alumnos] > cupo_maximo
        or grado2[cantidad_alumnos] > cupo_maximo
        or grado3[cantidad_alumnos] > cupo_maximo):
    print(f"Hay que abrir una nueva división.")
