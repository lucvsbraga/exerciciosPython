# @author: lucvsbraga
import random


qtd = int(input('Número de participantes: '))
nome = []
for i in range(qtd):
    nome.append(input(f'Digite {i+1}º nome: '))

print(f'Sorteado: {random.choice(nome)}')
