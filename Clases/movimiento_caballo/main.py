import os
from movimiento_caballo import MovimientoCaballo
from tablero_tui import mostrar_tablero

def limpiar_pantalla():
    os.system("cls")
    
def ingresar_opcion(texto, opciones):
    while (opcion := input(texto)) not in opciones:        
        pass
    return opcion

def preguntar_repetir():
    respuesta = ingresar_opcion("¿De nuevo? (S/N)", ("s", "S", "n", "N"))
    return respuesta.lower() == "s"

def modo_avance_manual():
    input("Presiones enter para continuar...")

def modo_avance_automatico():
    pass

def obtener_modo_avance():
    opcion = ingresar_opcion("Avance manual (1) o automático (2): ", ("1", "2"))
    modo_avance = modo_avance_automatico
    if opcion == "1":
        return modo_avance_manual
    return modo_avance
    
def limpiar_mostrar_tablero(movimientoCaballo):
    limpiar_pantalla()
    mostrar_tablero(movimientoCaballo)

def preguntar_de_nuevo():
    limpiar_pantalla()
    return preguntar_repetir()
    
if __name__ == "__main__":
    while (de_nuevo := preguntar_de_nuevo()):
        modo_avance = obtener_modo_avance()
        ancho = int(input("Ancho: "))
        alto = int(input("Alto: "))

        movimientoCaballo = MovimientoCaballo(ancho, alto)

        limpiar_mostrar_tablero(movimientoCaballo)
        while movimientoCaballo.mover_siguiente() is not None:
            modo_avance()
            limpiar_mostrar_tablero(movimientoCaballo)
        input("Presione enter para volver al menú...")