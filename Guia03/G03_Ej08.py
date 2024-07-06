"""
Una persona cautivada por los paisajes argentinos se le ocurrió la loca idea de unir los puntos mas extremos (Ushuahia
y La Quiaca) en bicicleta, es decir se propuso hacer 3641.3 Km en bicicleta.
Nuestro aventurero efectivamente inició la travesía pero se accidentó y solo recorrió x metros según su GPS.
Usted debe solicitar ese valor x e informar cuántos kilómetros y metros recorrió nuestro aventurero y qué porcentaje
representó lo recorrdo del total de Kms a recorrer de Ushuahia a La Quiaca (para el porcentaje usted deberá realizar
los calculos en metros).
"""

# Distancia total del viaje en Km
DISTANCIA_TOTAL_KM = 3641.3
DISTANCIA_TOTAL_M = DISTANCIA_TOTAL_KM * 1000

# Se pide la distancia que recorrió el aventurero en kilómetros
distancia_recorrdia_km = float(input("Ingrese la distancia recorrida (en Km): "))

# Se calcula la distancia recorrdia en metros
distancia_recorrdia_m = distancia_recorrdia_km * 1000

# Se calcula el porcentaje de de la distancia recorrida respecto a la total
porcentaje_recorrido = round(distancia_recorrdia_m * 100 / DISTANCIA_TOTAL_M, 2)

# Mostramos los resultados
print(f"Distancia recorrdia en kilómetros: {distancia_recorrdia_km}")
print(f"Distancia recorrdia en metros: {distancia_recorrdia_m}")
print(f"Porcentaje recorrdio en: {porcentaje_recorrido}%")




