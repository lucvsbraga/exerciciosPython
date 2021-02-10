# @author: lucvsbraga

from time import sleep
from random import randint

print('JO KEN PO')

computador = int(randint(1, 3))

print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
opcao = int(input('Opção: '))
mao = ['PEDRA', 'PAPEL', 'TESOURA']

if opcao > 0 and opcao < 4:
    sleep(.4)
    print('JO')
    sleep(.4)
    print('KEN')
    sleep(.4)
    print('PO')
    print('-' * 12)
    if computador == opcao:
        print(
            f'Você: {mao[opcao-1]} \nComputador: {mao[computador-1]}')
        print('-' * 12)
        print('Empate.')
    elif opcao == 1 and computador == 3:
        print(
            f'Computador jogou {mao[computador-1]} \nVocê jogou {mao[opcao-1]}')
        print('-' * 12)
        print('PEDRA > TESOURA')
        print('Você venceu.')
    elif opcao == 1 and computador == 2:
        print(
            f'Computador jogou {mao[computador-1]} \nVocê jogou {mao[opcao-1]}')
        print('-' * 12)
        print('PAPEL > PEDRA')
        print('O computador venceu.')
    elif opcao == 3 and computador == 1:
        print(
            f'Computador jogou {mao[computador-1]} \nVocê jogou {mao[opcao-1]}')
        print('-' * 12)
        print('PEDRA > TESOURA')
        print('O computador venceu.')
    elif opcao == 3 and computador == 2:
        print(
            f'Computador jogou {mao[computador-1]} \nVocê jogou {mao[opcao-1]}')
        print('-' * 12)
        print('TESOURA > PAPEL')
        print('Você venceu.')
    elif opcao == 2 and computador == 1:
        print(
            f'Computador jogou {mao[computador-1]} \nVocê jogou {mao[opcao-1]}')
        print('-' * 12)
        print('PAPEL > PEDRA')
        print('Você venceu.')
    elif opcao == 2 and computador == 3:
        print(
            f'Computador jogou {mao[computador-1]} \nVocê jogou {mao[opcao-1]}')
        print('-' * 12)
        print('TESOURA > PAPEL')
        print('O computador venceu.')
else:
    print('Opção inválida.')
