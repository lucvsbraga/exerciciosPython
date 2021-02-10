# @author: lucvsbraga

import os

opcao = 'A'
lista = []
par = []
impar = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
        
    opcao = input('Deseja continuar? [S/N]: ')
    
    if opcao in 'Nn':
        break
    elif opcao in 'Ss':
        os.system('clear')
        continue        
    else:
        print('Opção inválida.')
        break
    
os.system('clear')
print(f'Lista: {lista}')
print(f'Pares: {par}')
print(f'Ímpares: {impar}')