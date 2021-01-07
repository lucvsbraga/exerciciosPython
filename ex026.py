# @author: lucvsbraga

'''
Crie um algoritmo que conte o número de ocorrências de um caractere em uma string e mostre a posição da primeira e da última ocorrência.
'''

entrada = input('Digite uma frase: ')
busca = input('Digite a caractere que deseja buscar: ')
print('-' * 12)
print(f'Número de ocorrências: {entrada.upper().count(busca.upper())} ')
print(f'Primeira Ocorrência: {entrada.upper().find(busca.upper()) + 1}')
print(f'Última Ocorrência: {entrada.upper().rfind(busca.upper()) + 1}')
