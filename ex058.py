# @author: lucvsbraga

from random import randint

numero = randint(1, 10)
palpite = 0
i = 0

print('Pensei em um número de um a dez: ')
chances = int(input('Chances: '))

while palpite != numero and i < chances:
    palpite = int(input('Dê o seu palpite: '))
    i += 1
if palpite == numero:
    print('-' * 12)
    print(f'Você acertou: {numero}')
    print(f'Chances usadas: {i}')
else:
    print('-' * 12)
    print('Suas chances esgotaram.')
