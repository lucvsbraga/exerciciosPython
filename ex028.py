# @author: lucvsbraga

from random import randint
from time import sleep
numero = randint(0, 5)

print('Pensei em um número entre 0 e 5.')
palpite = int(input('Faça um palpite: '))
print('Loading...')
sleep(.3)
if numero == palpite:
    print(F'ACERTOU!!! {numero}')
else:
    print(f'Errou, o número que eu pensei foi: {numero}')
