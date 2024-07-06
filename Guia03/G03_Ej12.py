"""
En la disciplina olímpica una de las pruebas mas esperadas en la natación es la posta 4x100. En esta disciplina el
equipo ganador registró los siguientes tiempos en cada estilo:
    - Espalda: 52 segundos 15 centésimas.
    - Pecho: 1 minuto 2 segundos 75 centésimas.
    - Mariposa: 59 segundos 80 centésimas.
    - Libre: 48 segundos 15 centésimas.
Usted debe averguar el tiempo total de la carrera del equipo ganador y representarlo en minutos, segundos y centésimas.

Para recordar:
    - 1 minutos son 60 segundos.
    - 1 segundo son 100 centésimas.
"""

# Establecemos los datos con los que vamos a trabajar:
MINUTOS_ESPALDA = 0
SEGUNDOS_ESPALDA = 52
CENTESIMAS_ESPALDA = 15

MINUTOS_PECHO = 1
SEGUNDOS_PECHO = 2
CENTESIMAS_PECHO = 75

MINUTOS_MARIPOSA = 0
SEGUNDOS_MARIPOSA = 59
CENTESIMAS_MARIPOSA = 80

MINUTOS_LIBRE = 0
SEGUNDOS_LIBRE = 48
CENTESIMAS_LIBRE = 15

# Pasamos todos los datos a centesimas para facilitar las cuentas.
# Si hay 100 centesimas en un segundo, y 60 segundos en un minuto.
# Un minuto equivale a 100 * 60 centesimas.
centesimas_espalda = MINUTOS_ESPALDA * 6000 + SEGUNDOS_ESPALDA * 100 + CENTESIMAS_ESPALDA
centesimas_pecho = MINUTOS_PECHO * 6000 + SEGUNDOS_PECHO * 100 + CENTESIMAS_PECHO
centesimas_mariposa = MINUTOS_MARIPOSA * 6000 + SEGUNDOS_MARIPOSA * 100 + CENTESIMAS_MARIPOSA
centesimas_libre = MINUTOS_LIBRE * 6000 + SEGUNDOS_LIBRE * 100 + CENTESIMAS_LIBRE

# Obtenemos el total de la carrera (suma de todas las pruebas)
total_centesimas = centesimas_espalda + centesimas_mariposa + centesimas_pecho + centesimas_libre

# Representamos el total en formato (mm:ss:cc)
total_minutos = total_centesimas // 6000
total_segundos = total_centesimas % 6000 // 100
total_centesimas = total_centesimas % 6000 % 100

print(f"El tiempo total de la carrera fue {total_minutos}:{total_segundos}:{total_centesimas}")


