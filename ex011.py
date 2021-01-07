# @author: lucvsbraga

altura = float(input('Digite a altura em metros: '))
largura = float(input('Digite a largura em metros: '))
area = altura * largura

print(f'A parede contém uma área de {area}m².')
print(f'Serão necessárias {area / 2:.1f} latas de tinta para pintar a parede.')
