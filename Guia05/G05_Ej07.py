"""
Son muchas las concesionarias que en el último tiempo se han visto afectados por el poderoso virus PANTEVIL que ataca
los registros de automóviles, alterando el identificador de la patente de los mismos. Sabemos que el identificador de
patente de un automóvil está compuesto por 3 leetras en mayúsculas y 3 números, por ejemplo AED335.
Luego de un exhaustivo análisis de los registros infrectados, se logró decodificar cómo funciona el virus. Vamos a
separar en letras y números para explicar cómo codifica el virus:

Letras:
    - El virus transforma cada carácter en el entero Unicode al que representa.
    - Luego chequea si esos tres números son iguales, en caso afirmativo reemplaza los valores del primer y último
    número por valores aleatorios gneerados entre 65 y 90.
    - Una vez que tiene esos números, los convierte a cadena de caracteres y los concatena, anteponiendo:
        - Un signo @ en caso que los tres números hayan sido iguales
        - Un signo & en caso contrario.

Números:
    - Para codificar los números el virus utiliza una cadena con 5 caracteres
    - El primer carácter codifica:
        - Un signo + si los 3 números eran pares y les suma 1 a cada número.
        - Un signo - si los 3 números no son pares.
    - En el segundo carácter el virus pone:
        - Un signo # en caso que el primer número y el segundo son iguales, y cambia el valor de segundo número por el
        tercero.
        - Un signo $ en caso que el primero número y el tercero son iguales, y cambia el valor de tercer número por el
        segundo.
        - Un signo * en caso que el segundo número y el tercero son iguales, y cambia el valor de tercer número por el
        primero.
        - Un signo ! en caso que los 3 números sean diferentes.
    - En el tercero, cuarto y quinto caracter, el virus simplemente concaatena los números resultantes.

Finalmente y como si fuera poco, una vez codificados, el virus invierte el orden de los números y letras. Esto es
primero coloca los números codificados y luego las letras codificadas. Veamos algunos ejemplos:

Patente sin Virus   Patente con Virus
AED335              -#355&656968
PEP456              -!456&806980
RRR682              +!793@898280

Debido a la gravedad del caso, las concesionarias afectadas no pueden realizar ninguna venta hasta que no se reparen los
archivos dañados, es que nos han solicitado con urgegncia un reparador para el virus PANTEVIL.
"""

"""
ANÁLISIS

Como el virus lo que hace es invertir orden de números y letras, primero vamos a obtener los números y después las 
letras.
Números:
    El virus: 
    - Utiliza 5 caracteres para representar los 3 números de la patente.
    - Agrega un + al principio de la cadena si los 3 números y eran par y les suma 1 a cada uno, o un - si no lo eran.
    - El segundo caracter es el que nos va a indicar el valor de los 3 números originales.
        - Si el caracter es un #: El primer número actual representa los dos primeros originales, y el segundo número
        actual representa al tercero.
        - Si el caracter es un $: El primer número actual representa al primer y tercer número original, y el tercer
        número actual es igual al segundo original.
        - Si el caracter es un *: El segundo número actual es igual a los dos ultimos números originales, y el tercer
        número actual es igual al primero original.
        - Si el caracter es un !: Los 3 números actuales son diferentes entre ellos e iguales a los originales.

Letras: 
    - El virus transforma cada caracter en el entero Unicode al que representa y en base a los números agrega un 
    caracter antes de las letras.
    - Si el caracter es un @: Los tres enteros son iguales al segundo entero.
    - Si el caracter es un &: Cada número representa al caracter original.    
"""

# Pedimos al usuario que ingrese un número de patente con el virus
patente_virus = input("Ingrese una patente infectada: ")

# Procesos
# Determinamos los números de las patentes
# 1er caracter actual = 1er y 2do originales. - 2do caracter actual = 3er caracter orginal
if patente_virus[1] == "#":
    numero1, numero2, numero3 = patente_virus[2], patente_virus[2], patente_virus[3]
# 1er caracter actual = 1er y 3er originales. - 3er caracter actual = 2do caracter original
elif patente_virus[1] == "$":
    numero1, numero2, numero3 = patente_virus[2], patente_virus[4], patente_virus[2]
# 2do caracter actual = 2do y 3er originales. - 3er caracter actual = 1er caracter original
elif patente_virus[1] == "*":
    numero1, numero2, numero3 = patente_virus[4], patente_virus[3], patente_virus[3]
# Los números no cambiaron respecto al original
else:
    numero1, numero2, numero3 = patente_virus[2], patente_virus[3], patente_virus[4]

# Una vez que obtenemos los números, nos fijamos si hay que restarles uno a cada uno, o si los dejamos así.
if patente_virus[0] == "+":
    numero1 = str(int(numero1) - 1)
    numero2 = str(int(numero2) - 1)
    numero3 = str(int(numero3) - 1)

# Determinamos las letras
# Las 3 letras originales son iguales a la segunda actual en Unicode
if patente_virus[5] == "@":
    letra1 = chr(int(patente_virus[8] + patente_virus[9]))
    letra2, letra3 = letra1, letra1
# Las 3 letras son las mismas que las actuales en Unicode
else:
    letra1 = chr(int(patente_virus[6] + patente_virus[7]))
    letra2 = chr(int(patente_virus[8] + patente_virus[9]))
    letra3 = chr(int(patente_virus[10] + patente_virus[11]))

patente_original = letra1 + letra2 + letra3 + numero1 + numero2 + numero3

print(f"Patente con Virus\t\tPatente sin Virus\n"
      f"{patente_virus}\t\t\t{patente_original}")
