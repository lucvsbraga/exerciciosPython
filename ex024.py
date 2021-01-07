# @author: lucvsbraga

'''
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome: "Belo"
'''

cidade = input('Digite uma cidade: ').strip()
print(cidade[:4].upper() == 'BELO')
