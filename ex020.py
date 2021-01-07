# @author: lucvsbraga
from random import shuffle

lista = []
qtd = int(input('Digite o número de elementos da lista: '))

for i in range(qtd):
    lista.append(input(f'Inserir item {i+1}: '))

print('-' * 12)
shuffle(lista)
print(f'Nova ordem: {lista}')
