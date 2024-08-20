

























def factorial(n):
    if n == 1 or n == 0:
        return 1

    uno_menos = n - 1
    return n * factorial(uno_menos)

print(factorial(5))