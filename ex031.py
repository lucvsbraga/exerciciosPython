# @author: lucvsbraga

distancia = float(input('Distância da viagem: '))
print('-' * 12)
if distancia <= 200:
    print(f'Preço: R${distancia * 0.5:.2f}')
else:
    print(f'Preço: R${distancia * 0.45:.2f}')
