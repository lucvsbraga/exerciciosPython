# @author: lucvsbraga

'''
Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e 
a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa
R$ 60 por dia a R$0,15 por KM rodado.
'''

dias = int(input('Digite o número de dias com o carro alugado: '))
km = float(input('Digite a quantidade de km percorridos: '))
print('-' * 12)
total = (dias * 60) + (km * 0.15)
print(f'Total a pagar: R$ {total:.2f}')
