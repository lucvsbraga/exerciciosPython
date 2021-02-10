# @author: lucvsbraga
import os
produto = []
preco = []

while True:
    os.system('clear')
    produto.append(input('Nome: '))
    preco.append(float(input('Preço: ')))

    resp = ' '
    while resp not in 'SN':
        resp = input('Continua? (S/N): ').strip().upper()[0]
    if resp in 'Nn':
        break

menor = preco.index(min(preco))

os.system('clear')
for i in range(len(preco)):
    if preco[i] > 1000:
        print(f'Nome: {produto[i]} R${preco[i]:.2f} <= *produtos acima de 1k')    

print(f'Produto mais barato: {produto[menor]} R${min(preco):.2f}')
print('=' * 12  + ' Fim ' + '=' * 12)
print(f'Total: R${sum(preco):.2f}')
