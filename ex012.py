# @author: lucvsbraga

preco = float(input('Informe o preço: R$'))
desconto = float(input('Informe o desconto: '))
print('-' * 12)
print(f'Valor sem desconto: {preco}')
print(f'Valor com desconto: {preco - (preco * desconto / 100)}')
