# Configuración
# ((Encabezado, Longitud, justificación))



def borde(columnas, izquierda, centro, derecha):
    borde = izquierda 
    for columna in columnas[:-1]:
        borde += "═" * columna[1] + centro
    
    borde += "═" * columnas[-1][1] + derecha
    return borde

def borde_superior(columnas):
    return borde(columnas, "╔", "╦", "╗")

def borde_inferior(columnas):
    return borde(columnas, "╚", "╩", "╝")

def fila(columnas, dato):
    fila = ""
    for i, campo in enumerate(dato):
        ancho = columnas[i][1]
        justificacion = columnas[i][2]
        fila += "║" + f"{str(campo):{justificacion}{ancho}.{ancho}}"
    return fila + "║"

def separador(columnas):
    separador_texto = "╠"
    for columna in columnas[:-1]:
        separador_texto += "═" * columna[1] + "╬" 
    separador_texto += "═" * columnas[-1][1] + "╣"
    return separador_texto 


def filas(columnas, datos):
    texto_filas = ""
    for dato in datos:
        texto_filas += separador(columnas) + "\n"
        texto_filas += fila(columnas, dato) + "\n"
    
    return texto_filas

def encabezado(columnas):
    nombres = tuple(columna[0] for columna in columnas) 
    return fila(columnas, nombres)


def grilla(columnas, datos):
    texto_grilla = borde_superior(columnas) + "\n"
    texto_grilla += encabezado(columnas) + "\n"
    texto_grilla += filas(columnas, datos) 
    texto_grilla += borde_inferior(columnas)
    print(texto_grilla)
    
if __name__ == "__main__": 
    columnas = (("Nombre", 20, "<"), ("Apellido", 20, "<"), ("Edad", 4, ">"))
    grilla(columnas, [["Pablo", "Villalba", 42], ["Juan", "Pérez", 18]])