# @author: lucvsbraga

peso = []

for i in range(5):
    peso.append(float(input(f'Peso da {i + 1}ª pessoa: ')))

print(f'Maior: {max(peso)}')
print(f'Menor: {min(peso)}')
