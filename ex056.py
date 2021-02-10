# @author: lucvsbraga

nome = []
idade = []
sexo = []
idadeHomem = []
aux = 0
for i in range(4):
    print('=' * 12 + f'{i+1}ª pessoa' + '=' * 12)
    nome.append(input('Nome: '))
    idade.append(int((input('Idade: '))))
    sexo.append((input('Sexo (F/M)): ').strip()))
    if sexo[i] in 'Ff' and idade[i] < 20:
        aux += 1
    elif sexo[i] in 'Mm':
        idadeHomem.append(idade[i])

avgIdade = sum(idade) / len(idade)

print('=' * 12)
print(f'Homem mais velho: {max(idadeHomem)}')
print(f'Média da idade do grupo: {avgIdade:.0f}')
print(f'Número de mulheres com menos de 20 anos: {aux}')
