import soporte


def contar_apariciones_por_indice(lista):
    numeros = [0] * 300000
    for elemento in lista:
        numeros[elemento] += 1
    return numeros


def contar_elementos_menos_cero(lista):
    contador = 0
    for elemento in lista:
        if elemento != 0:
            contador += 1
    return contador


def calcular_valor_modal(lista):
    mayor = 0
    for i in range(1, len(lista)):
        if lista[mayor] < lista[i]:
            mayor = i
    return mayor


def principal():
    v = soporte.vector_known_range(300000)

    """Consigna 1"""
    # Calcular cantidad de números diferentes generados en v
    numeros = contar_apariciones_por_indice(v)
    contador = contar_elementos_menos_cero(numeros)
    print(contador)

    """Consigna 2"""
    # Calcular el valor modal de v
    moda = calcular_valor_modal(numeros)
    print(moda)

    """Consigna 3"""
    # Calcular frecuencia de aparición del valor modal
    print(numeros[moda])





if __name__ == '__main__':
    principal()