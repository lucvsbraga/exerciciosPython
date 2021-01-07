# @author: lucvsbraga

from math import pow, sqrt, hypot

cateto_oposto = float(input('Comrpimento do cateto oposto: '))
cateto_adj = float(input('Comprimento do cateto adjacente: '))

# hipotenusa = sqrt((pow(cateto_oposto, 2) + pow(cateto_adj, 2)))
hipotenusa = hypot(cateto_oposto, cateto_adj)
print('-' * 12)
print(f'Hipotenusa: {hipotenusa:.2f}')
