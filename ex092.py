# @author: lucvsbraga

from datetime import date
import datetime
trabalhador = {}
trabalhador['nome'] = input('Nome: ')
trabalhador['idade'] = date.today().year - int(input('Ano de nascimento: '))
trabalhador['ctps'] = int(input('Carteira de Trabalho: '))
if trabalhador['ctps'] != 0:
  trabalhador['anoContratacao'] = int(input('Ano de Contratação: '))
  trabalhador['salario'] = float(input('Salário: '))
  trabalhador['idadeAposentadoria'] = trabalhador['idade'] + ((trabalhador['anoContratacao'] + 35) - date.today().year)

print(trabalhador)