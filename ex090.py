# @author: lucvsbraga
import os

aluno = {}
aluno['Nome'] = input('Nome: ')
aluno['Média'] = float(input('Média: '))

if aluno['Média'] < 5:
    aluno['Situação'] = 'Reprovado'
elif aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Aprovado'


os.system('clear')
for k, v in aluno.items():
    print(f'{k}: {v}')
