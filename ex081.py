# @author: lucvsbraga

import os

opcao = 'A'
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    opcao = input('Deseja continuar? [S/N]: ')
    if opcao in 'Nn':
        break
    elif opcao in 'Ss':
        continue
    else:
        print('Opção inválida.')
        break
    os.system('cls')
print(f'Você digitou {len(lista)} números.')
if 5 in lista:
    print(f'O número 5 está na {lista.index(5)+1}ª posição.')
else:
    print('O 5 não está na lista.')
lista.sort(reverse = True)
print(f'Lista ordenada decrescente: {lista}')
