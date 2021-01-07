# @author: lucvsbraga

from datetime import date
print('Digite 0 para analisar o ano atual.')
ano = int(input('Ano: '))
print('-' * 12)

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')
