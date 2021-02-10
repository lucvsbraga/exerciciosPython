# @author: lucvsbraga
from datetime import date

menor = 0
maior = 0
for i in range(7):
    n = int(input(f'Ano de nascimento da {i+1}ª pessoa:'))
    c = date.today().year
    if c - n < 18:
        menor += 1
    else:
        maior += 1

print('-' * 12)
print(f'Menores: {menor}')
print(f'Maiores: {maior}')
