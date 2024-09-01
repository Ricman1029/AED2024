import random

def generar_bolillero():
    bolillero = [False] * 90
    return bolillero

def sacar_nro(bolillero):
    i = 0
    disponibles=[]
    for e in bolillero:
        if not e:
            disponibles.append(i)
        i += 1
        
    valor=random.choice(disponibles)
    bolillero[valor] = True
    
    return valor


