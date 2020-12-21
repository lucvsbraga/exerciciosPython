# @author: lucvsbraga

'''
Escreva um programa que converta uma temperatura digitada em °C e converta para °F.
'''

c = float(input('Informe a temperatura em C°: '))
f = ((9 * c) / 5) + 32
print('-' * 12)
print(f'C°: {c:.1f}')
print(f'F°: {f:.1f}')