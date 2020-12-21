# @author: lucvsbraga

'''
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, 
cosseno e tangente desse ângulo.
'''
from math import sin, cos, tan, radians

angulo = float(input('Digite um ângulo: '))
print('-' * 12)
print(f'Seno: {sin(radians(angulo)):.2f}')
print(f'Cosseno: {cos(radians(angulo)):.2f}')
print(f'Tangente: {tan(radians(angulo)):.2f}')
