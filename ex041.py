# @author: lucvsbraga

from datetime import date

ano_atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = ano_atual - nascimento

print('-' * 12)
print(f'Idade: {idade}')
if idade <= 9:
    print('Categoria: Mirim')
elif idade <= 14:
    print('Categoria: Infantil')
elif idade <= 19:
    print('Categoria: Júnior')
elif idade <= 25:
    print('Categoria: Sênior')
else:
    print('Categoria: Master')
