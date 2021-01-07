# @author: lucvsbraga

'''
Faça um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e o último nome separadamente.
    Ex: Fulano da Silva Sauro
        Nome: Fulano
        Sobrenome: Sauro
'''

nome = input('Digite seu nome completo: ').strip()
nome = nome.split()
print('-' * 12)
print(f'Nome: {nome[0]}')
print(f'Sobrenome: {nome[len(nome)-1]}')
