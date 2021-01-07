# @author: lucvsbraga

'''
Crie um programa que leia o nome completo de uma pessoa e mostre:

> O nome com todas as letras maiúsculas e minúsculas.
> Quantas letras ao todo (sem considerar espaços).
> Quantas letras tem o primeiro nome.
'''

nome = str(input('Digite o nome completo: ')).strip()
print(f'UPPER: {nome.upper()}')
print(f'LOWER: {nome.lower()}')
primeiro_nome = nome.find(' ')
total = len(nome) - nome.count(' ')
print(f'Número de letras primeiro nome: {primeiro_nome}')
print(f'Total de letras: {total}')
