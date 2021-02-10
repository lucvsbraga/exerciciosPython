# @author: lucvsbraga

from datetime import date

nascimento = int(input('Digite sua data de nascimento: '))
ano_atual = date.today().year

idade = (ano_atual - nascimento)

alistamento = idade - 18
print(f'Idade: {idade}')

if alistamento > 0:
    print(f'Você não se alistou e está {alistamento} anos atrasado.')
else:
    print(f'Faltam {abs(alistamento)} anos para você se alistar.')
