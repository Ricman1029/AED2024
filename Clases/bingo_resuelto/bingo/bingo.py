import os

from gererar_carton import generar_carton
from generar_bolillero import generar_bolillero, sacar_nro
from bolillero_ui import dibujar_bolillero
from carton_ui import dibujar_carton

def limpiar_pantalla():
    os.system("cls")


def actualizar_carton(carton, numero):
    decena = numero // 10
    for i in range(0, 3):
        if carton[i][decena] is not None and carton[i][decena][0] == numero:
            carton[i][decena] = (carton[i][decena][0], True)
    

cartones = [generar_carton(), generar_carton(), generar_carton(), generar_carton()]

bolillero = generar_bolillero()


for i in range(0, 90):
    limpiar_pantalla()
    numero = sacar_nro(bolillero)
    dibujar_bolillero(bolillero)
    for carton in cartones:
        actualizar_carton(carton, numero)
        dibujar_carton(carton)
    input()
    

dibujar_bolillero(bolillero)

