# @author: lucvsbraga

notas = []

notas.append(float(input('Digite a primeira nota: ')))
notas.append(float(input('Digite a segunda nota: ')))

media = sum(notas) / len(notas)
print('-' * 12)
print(f'Média: {media}')
if media < 5:
    print('Status: reprovado.')
elif media < 7:
    print('Status: recuperação.')
else:
    print('Status: aprovado.')
