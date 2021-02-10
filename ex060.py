# @author: lucvsbraga
from math import factorial
print('=' * 12 + ' FATORIAL ' + '=' * 12)
n = int(input('Número: '))

for i in range(1, n+1, 1):
    print(factorial(i), end=' ')


def fatorial_recursivo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fatorial_recursivo(n - 1) * n
