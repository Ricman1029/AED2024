def son_anagrama(palabra1, palabra2):
    if len(palabra1) != len(palabra2):
        return False
    if palabra1.lower() == palabra2.lower():
        return False
    for caracter1 in palabra1:
        for caracter2 in palabra2:
            if caracter1 == caracter2:
                palabra1 = palabra1.replace(caracter1, "")
                palabra2 = palabra2.replace(caracter1, "")
                break

    return True if len(palabra1) == 0 else False


def principal():
    palabra1 = input("Ingrese la primer palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")

    if son_anagrama(palabra1, palabra2):
        print("Sí son angagrama.")
    else:
        print("Não não")


if __name__ == '__main__':
    principal()