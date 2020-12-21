# @author: lucvsbraga

'''
Escreva um programa que leia um valor em metros e o exiba convertido em:
km, hm, dam, m, dm, cm, mm
'''

metros = int(input('Digite a medida em metros: '))

print(f'Metros: {metros}')
print(f'mm: {metros * 1000:.0f} ')
print(f'cm: {metros * 100:.0f}')
print(f'dm: {metros * 10:.0f}')
print(f'dam: {metros / 10}')
print(f'hm: {metros /100}')
print(f'km: {metros / 1000}')
