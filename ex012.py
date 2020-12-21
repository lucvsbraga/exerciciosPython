# @author: lucvsbraga

'''
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''

preco = float(input('Informe o preço: R$'))
desconto = float(input('Infomre o desconto: '))
print('-' * 12)
print(f'Valor sem desconto: {preco}')
print(f'Valor com desconto: {preco - (preco * desconto / 100)}')