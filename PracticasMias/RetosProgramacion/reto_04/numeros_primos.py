def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True


def principal():
    for i in range(100):
        if es_primo(i):
            print(i)


if __name__ == '__main__':
    principal()