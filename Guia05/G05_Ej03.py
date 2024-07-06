"""
El Área de Mantinimiento de un laboratorio informático nos ha solicitado el desarrollo de un programa que facilite la
gestión de las tareas realizadas en el día.
El usuario debe ingresar de tres equipos informáticos (PC) los siguientes datos: número de indentificación de la PC,
tiempo de reparación (expresado en minutos) y la cusa de mantenimiento (1- Problema de Hardware 2- Problema de Software)

Los requerimientos funcionales son:
    a) ¿Cuál es el tiempo total de las tareas de mantenimiento?
    b) ¿Cuál es el PC (número de identificación) que tuvo mayor tiempo en tareas de mantenimiento?
    c) Tiempo promedio de tareas de mantenimiento.
    d) Informar con un mensaje si todas la PC (número de identificación) que se les ha realizado mantenimiento tuvieron
    problemas de Hardware.
"""

# Carga de datos
equipo1 = input("Ingrese el número de identificación de la primer PC: "), \
    int(input("Ingrese el tiempo de reparacion (en minutos): ")), \
    int(input("Ingrese la causa de mantenimiento (1- Problema de Hardware. 2- Problema de Software): "))

equipo2 = input("Ingrese el número de identificación de la segunda PC: "), \
    int(input("Ingrese el tiempo de reparacion (en minutos): ")), \
    int(input("Ingrese la causa de mantenimiento (1- Problema de Hardware. 2- Problema de Software): "))

equipo3 = input("Ingrese el número de identificación de la tercer PC: "), \
    int(input("Ingrese el tiempo de reparacion (en minutos): ")), \
    int(input("Ingrese la causa de mantenimiento (1- Problema de Hardware. 2- Problema de Software): "))

# Procesos
horas_totales = equipo1[1] // 60 + equipo2[1] // 60 + equipo3[1] // 60
minutos_totales = equipo1[1] % 60 + equipo2[1] % 60 + equipo3[1] % 60
tiempo_total = f"{horas_totales}:{minutos_totales}"

if equipo1[1] < equipo2[1]:
    equipo1, equipo2 = equipo2, equipo1
if equipo1[1] < equipo3[1]:
    equipo1, equipo3 = equipo3, equipo1

promedio_minutos = (equipo1[1] + equipo2[1] + equipo3[1]) / 3
promedio_horas_totales = promedio_minutos // 60
promedio_minutos_totales = promedio_minutos % 60

# Muestra de datos
print(f"{equipo1[0]} tuvo el mayor tiempo de mantenimiento.")
print(f"El tiempo total de tareas de mantenimiento fue {tiempo_total}")
if equipo1[2] == 1 and equipo2[2] == 1 and equipo3[2] == 1:
    print("Todos tuvieron problemas de hardware.")
else:
    print("No todos tuvieron problemas de hardware.")
