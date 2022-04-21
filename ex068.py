# @author: lucvsbraga

from random import randint
import os
choice = 'm'
n = -4
c = 0
    
print('JOGO DO PAR OU ÍMPAR')

while True:
    pc = randint(0, 11)

    while choice not in 'PI':
        choice = input('Par ou Ímpar: ').strip().upper()[0]
        
    while n < 0 or n > 10:
        n = int(input('Número (0/10): '))
        
    if choice == 'P' and (pc + n) % 2 == 0:
        c += 1
        os.system('cls')
        print(f'Você escolheu: P')
        print(f'Você: {n} | PC: {pc}')
        print(f'Você ganhou. [{c}]')                
    elif choice == 'I' and (pc + n) % 2 == 1:
        c += 1
        os.system('cls')
        print(f'Você escolheu: I')
        print(f'Você: {n} | PC: {pc}')
        print(f'PC: {pc}')
        print(f'Você ganhou. [{c}]')
    else:
        os.system('cls')
        print(f'Você escolheu: {choice}')
        print(f'Você: {n} | PC: {pc}')
        print(f'Você perdeu após {c} vitórias.')  
        break
