# @author: lucvsbraga

'''
Mostre o menor e maior número entre os 3 informados pelo usuário.
'''

num = []

num.append(float(input('Primeiro número: ')))
num.append(float(input('Segundo número: ')))
num.append(float(input('Terceiro número: ')))

print('-' * 12)

print(f'Menor: {min(num)}')
print(f'Maior: {max(num)}')
