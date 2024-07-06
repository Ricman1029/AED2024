# contador total de palabras
ctp = 0
# contador de letras en una palabra
cl = 0
# contador de palabras que empiezan con p
cpp = 0
# contador de palabras que tuvieron "ta"
cta = 0
# flag: la ultima letra fue una "t"?
st = False
# flag: se ha formado la silaba "ta" al menos una vez?
sta = False
car = None
while car != '.':
    # cargar y procesar el caracter ingresado en car
    car = input('Letra (con "." termina):  ')
    cl += 1
    # final de palabra?
    if car == ' ' or car == '.':
        # ha terminado una palabra...
        # ...contarla solo si hubo al menos una letra...
        if cl > 1:
            ctp += 1
        # si hubo "ta" contar la palabra...
        if sta == True:
            cta += 1
        # ...reiniciar contador de letras (por próxima palabra)...
        cl = 0
        # reiniciar flags (por próxima palabra)...
        st = sta = False
    else:
        # car es una letra... la palabra sigue...
        # ...contar la palabra si comienza con "p"...
        if cl == 1 and car == 'p':
            cpp += 1
        # ...deteccion de la silaba "ta"...
        if car == 't':
            st = True
        else:
            # hay una "a" y la anterior fue una "t"?...
            if car == 'a' and st == True:
                sta = True
            st = False
print('Cantidad de palabras:', ctp)
print('Cantidad de palabras que empiezan con "p":', cpp)
print('Cantidad de palabras que contienen "ta":', cta)