# @author: lucvsbraga

'''
Escreva um algorítimo conversor de moedas.
'''

real = float(input('Digite o valor em reais: R$ '))
dolar = float(input('Cotação do dólar: USD '))

print(f'Saldo em reais: {real}')
print(f'Saldo em dólar: {real / dolar:.2f}')