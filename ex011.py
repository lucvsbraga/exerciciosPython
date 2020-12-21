# @author: lucvsbraga

'''
Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
'''

altura = float(input('Digite a altura em metros: '))
largura = float(input('Digite a largura em metros: '))
area = altura * largura

print(f'A parede contém uma área de {area}m².')
print(f'Serão necessárias {area / 2:.1f} latas de tinta para pintar a parede.')
