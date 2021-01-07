# @author: lucvsbraga

'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre - e 5 e peça para o 
usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na 
tela se o usuário venceu ou perdeu.
'''


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
