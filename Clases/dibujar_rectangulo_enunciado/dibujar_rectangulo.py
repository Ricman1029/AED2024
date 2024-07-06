ALTO = 10
ANCHO = 35
ESTILO = "3;30;43"

formato = f"\x1b[{ESTILO}m%s\x1b[0m"
horizontal_superior = "┌" + "─" * ANCHO + "┐"
lineas_verticales = "│" + " " * ANCHO + "│"
horizontal_inferior = "└" + "─" * ANCHO + "┘"

print(formato % horizontal_superior)
texto = (formato + "\n") * ALTO % ((lineas_verticales,) * ALTO)
print(texto, end="") 
print(formato % horizontal_inferior)
