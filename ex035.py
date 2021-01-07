# @author: lucvsbraga

'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não 
formar um triângulo.
'''

a = float(input('Comprimento da primeira reta: '))
b = float(input('Comprimento da segunda reta: '))
c = float(input('Comprimento da terceira reta: '))
print('-' * 12)

if a < b + c and b < c + a and c < b + a:
    print('Essas retas podem formar um triângulo.')
else:
    print('Essas retas não pode formar um triângulo.')
