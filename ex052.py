# @author: lucvsbraga

n = int(input('Digite um número: '))
cont = 0

for i in range(1, n, 1):
    if n % i == 0:
        cont += 1

if cont > 2:
    print('Não é um número primo.', end='')
    print('oi')
else:
    print('É um número primo.')
