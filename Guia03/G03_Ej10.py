"""
Un triatlón es una competición deportiva en que los participantes realizan tres carreras: una de natación, una ciclista
y una pedestre.
Desarrollar un programa que permita ingresar el tiempo (en minutos y segundos) logrados en cada etapa por uno de los
deportistas participantes.
Con esos datos determinar:
- Tiempo total de la prueba (en formato hh:mm:ss)
- Tiempo máximo y mínimo (en segundos)
- Tiempo promedio de la prueba (en segundos, redondeado a 2 decimales)

Consejo: convertir a segundos los horarios ingresados para facilitar las operaciones.
"""

# Carga de datos
tiempo_natacion = input("Ingresar tiempo logrado en natación (mm:ss): ")
tiempo_ciclismo = input("Ingresar tiempo logrado en ciclismo (mm:ss): ")
tiempo_pedestre = input("Ingresar tiempo logrado en pedestre (mm:ss): ")

# Obtenemos minutos y segundos para cada prueba
minutos_natacion = int(tiempo_natacion[0] + tiempo_natacion[1])
segundos_natacion = int(tiempo_natacion[3] + tiempo_natacion[4])
minutos_ciclismo = int(tiempo_ciclismo[0] + tiempo_ciclismo[1])
segundos_ciclismo = int(tiempo_ciclismo[3] + tiempo_ciclismo[4])
minutos_pedestre = int(tiempo_pedestre[0] + tiempo_pedestre[1])
segundos_pedestre = int(tiempo_pedestre[3] + tiempo_pedestre[4])

# Pasamos todos los tiempos de las pruebas a cantidad total de segundos para facilitar las operaciones
total_segundos_natacion = minutos_natacion * 60 + segundos_natacion
total_segundos_ciclismo = minutos_ciclismo * 60 + segundos_ciclismo
total_segundos_pedestre = minutos_pedestre * 60 + segundos_pedestre

# Con estos podemos determinar:
# Tiempo total de la prueba = suma de los tiempo de las 3 pruebas en segundos
total_triatlon = total_segundos_natacion + total_segundos_ciclismo + total_segundos_pedestre

# Lo formateamos a (hh:mm:ss)
total_horas = total_triatlon // 3600
total_minutos = total_triatlon % 3600 // 60
total_segundos = total_triatlon % 3600 % 60
tiempo_total_triatlon = f"{total_horas}:{total_minutos}:{total_segundos}"

# Tiempo máximo y mínimo
tiempo_max = max(total_segundos_natacion, total_segundos_ciclismo, total_segundos_pedestre)
tiempo_min = min(total_segundos_natacion, total_segundos_ciclismo, total_segundos_pedestre)

# Tiempo promedio
tiempo_promedio = round(total_triatlon / 3, 2)

print(f"El tiempo total de la prueba fue de {tiempo_total_triatlon}")
print(f"El tiempo mínimo de la pruebas fue {tiempo_min} segundos.")
print(f"El tiempo máximo de la pruebas fue {tiempo_max} segundos.")
print(f"El tiempo promedio de la prueba fue {tiempo_promedio} segundos.")
