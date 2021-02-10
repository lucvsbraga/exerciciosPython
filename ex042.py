# @author: lucvsbraga

a = float(input('Comprimento da primeira reta: '))
b = float(input('Comprimento da segunda reta: '))
c = float(input('Comprimento da terceira reta: '))
print('-' * 12)

if a < b + c and b < c + a and c < b + a:
    print('Essas retas podem formar um triângulo ')
    if a != b != c != a:
        print('escaleno.')
    if a == b == c:
        print('equilátero.')
    else:
        print('isóceles.')
else:
    print('Essas retas não pode formar um triângulo.')
