"""
Se desea un programa que dados 2 ángulos expresados en grados minutos y segundos, informe la suma de ambos en grados
minutos y segundos.
"""

# Carga de datos
angulo1 = input("Ingrese el ángulo 1 (ggºmm'ss''): ")
angulo2 = input("Ingrese el ángulo 2 (ggºmm'ss''): ")

# Obtenemos los grados, minutos y segundos de los ángulos
grados_angulo1 = int(angulo1[0] + angulo1[1])
minutos_angulo1 = int(angulo1[3] + angulo1[4])
segundos_angulo1 = int(angulo1[6] + angulo1[7])

grados_angulo2 = int(angulo2[0] + angulo2[1])
minutos_angulo2 = int(angulo2[3] + angulo2[4])
segundos_angulo2 = int(angulo2[6] + angulo2[7])

# Convertimos los angulos a segundos
total_segundos_angulo1 = grados_angulo1 * 3600 + minutos_angulo1 * 60 + segundos_angulo1
total_segundos_angulo2 = grados_angulo2 * 3600 + minutos_angulo2 * 60 + segundos_angulo2

# Sumamos segundos
suma_segundos_totales = total_segundos_angulo1 + total_segundos_angulo2

# Convertimos suma a sexagésimal
grados_suma = suma_segundos_totales // 3600
minutos_suma = suma_segundos_totales % 3600 // 60
segundos_suma = suma_segundos_totales % 3600 % 60

# Mostramos los resultados
print(f"El resultado de la suma es {grados_suma}º{minutos_suma}'{segundos_suma}\"")

