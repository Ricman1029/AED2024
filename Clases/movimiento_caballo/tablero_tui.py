def borde(columnas, izquierda, centro, derecha):
    borde = izquierda 
    for columna in columnas[:-1]:
        borde += "═" * columna[0] + centro
    
    borde += "═" * columnas[-1][0] + derecha
    return borde

def borde_superior(columnas):
    return borde(columnas, "╔", "╦", "╗")

def borde_inferior(columnas):
    return borde(columnas, "╚", "╩", "╝")

def fila(columnas, dato):
    fila = ""
    for i, campo in enumerate(dato):
        ancho = columnas[i][0]
        justificacion = columnas[i][1]
        fila += "║" + f"{campo}"
    return fila + "║"

def separador(columnas):
    separador_texto = "╠"
    for columna in columnas[:-1]:
        separador_texto += "═" * columna[0] + "╬" 
    separador_texto += "═" * columnas[-1][0] + "╣"
    return separador_texto 

def filas(columnas, datos):
    texto_filas = fila(columnas, datos[0]) + "\n"
    for dato in datos[1:]:
        texto_filas += separador(columnas) + "\n"
        texto_filas += fila(columnas, dato) + "\n"
    
    return texto_filas

def grilla(columnas, datos):
    texto_grilla = borde_superior(columnas) + "\n"
    texto_grilla += filas(columnas, datos) 
    texto_grilla += borde_inferior(columnas)
    print(texto_grilla)

def mostrar_tablero(movimientoCaballo):
    tablero = [[f"{"  " if celda.orden == 0 else celda.orden  :>3}" for celda in fila] for fila in movimientoCaballo.tablero]
    fila = movimientoCaballo.celda_actual.posicion.fila
    columna = movimientoCaballo.celda_actual.posicion.columna
    tablero[fila][columna] = "\033[91m{0:>3}\033[0m".format(tablero[fila][columna])
    grilla([(3, ">")] * movimientoCaballo.ancho, tablero)
