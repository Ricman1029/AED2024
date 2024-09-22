def principal():
    primero = 0
    segundo = 1
    for i in range(50):
        print(f"{i + 1}: {primero}")

        siguiente = primero + segundo
        primero, segundo = segundo, siguiente


if __name__ == '__main__':
    principal()