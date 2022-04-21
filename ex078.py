#  @author: lucvsbraga
import os
lista = []
for i in range(5):
    lista.append(int(input(f'[{i+1}] - Digite um número: ')))

os.system('cls')
print(f'Maior: {max(lista)} na {lista.index(max(lista))+1}ª posição.')
print(f'Menor: {min(lista)} na {lista.index(min(lista))+1}ª posição.')