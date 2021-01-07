# @author: lucvsbraga

nome = input('Digite seu nome completo: ').strip()
nome = nome.split()
print('-' * 12)
print(f'Nome: {nome[0]}')
print(f'Sobrenome: {nome[len(nome)-1]}')
