import soporte
from funciones import buscar_indice, ordenar_lista


def contar_elementos_diferentes(lista):
    numeros = []
    contador = []

    for elemento in lista:
        indice = buscar_indice(numeros, elemento)
        if indice is None:
            numeros.append(elemento)
            contador.append(1)
        else:
            contador[indice] += 1

    return numeros, contador


def principal():
    v = soporte.vector_unknown_range(300000)

    """Consigna 1"""
    # Calcular cantidad de números diferentes generados en v
    numeros, contador = contar_elementos_diferentes(v)
    print(len(numeros), len(contador))

    """Consigna 2"""
    # Calcular el valor modal de v
    contador_ordenado = ordenar_lista(contador)
    moda = contador_ordenado[0] if contador_ordenado[0] != contador_ordenado[1] else 0
    valor_modal = numeros[buscar_indice(contador, moda)]
    print(valor_modal)

    """Consigna 3"""
    # Calcular la frecuencia de aparición del valor modal
    print(contador_ordenado[0])


if __name__ == '__main__':
    principal()