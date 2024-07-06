def parcial_parametros(parametros_str):
    longitud = len(parametros_str)
    i = 0
    ancho, alto, estilo = 25, 15, "3;30;44"

    # Avanzo caracter a caracter asignandoselo a la variable c
    while i < longitud:
        c = parametros_str[i]
        nombre = ""
        # Le asignamos el nombre del parametro que vamos a actualizar a la variable "nombre"
        while i < longitud and c != "=":
            nombre += c
            i += 1
            c = parametros_str[i]
        # Esto (i += 1) es para saltearme el caracter que es igual a "=" ya que no me interesa
        i += 1
        c = parametros_str[i]
        valor = ""
        # Le asignamos el valor del parametro que vamos a cambiar a la variable valor
        while i < longitud and c != ",":
            valor += c
            i += 1
            if i < longitud:
                c = parametros_str[i]
        # Esto(i += 1) es para saltearme el caracter que es igual a "," ya que no me interesa
        i += 1

        # Vamos actualizando las 3 variables que tenmos que cambiar
        if nombre == "ANCHO":
            ancho = int(valor)
        elif nombre == "ALTO":
            alto = int(valor)
        elif nombre == "ESTILO":
            estilo = valor

    return ancho, alto, estilo


with open("configuracion.txt", "r", encoding="utf-8") as archivo:
    configuracion = archivo.readline()
    ANCHO, ALTO, ESTILO = parcial_parametros(configuracion)

formato = f"\x1b[{ESTILO}m%s\x1b[0m"
horizontal_superior = "┌" + "─" * ANCHO + "┐"
lineas_verticales = "│" + " " * ANCHO + "│"
horizontal_inferior = "└" + "─" * ANCHO + "┘"

print(formato % horizontal_superior)
print((formato + "\n") * ALTO % ((lineas_verticales, ) * ALTO), end="")
print(formato % horizontal_inferior)
