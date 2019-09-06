import time
def fibonacci_recursivo(n):
    n1 = 1
    n2 = 1
    termo = 1
    if n > 2:
        termo = fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)
    return termo

numeros = [10, 20, 30, 40]

tempo = 0

for i in numeros:
    ini = time.time()
    rec = fibonacci_recursivo(i)
    fim = time.time()

    tempo += (fim - ini)

    print('Fibonacci(%d): %d' % (i, rec))

print('Tempo Gasto: %.1f\n' % tempo)