# @author: lucvsbraga

'''
Crie um algorítmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
'''
import math
num = input('Digite um número: ')
raiz = math.sqrt(float(num))
print(f'Dobro: {float(num) * 2 } \nTriplo: {float(num) * 3} \nRaiz quadrada: {raiz}')