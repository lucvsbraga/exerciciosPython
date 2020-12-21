# @author: lucvsbraga

'''
Faça um algorítmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''

salario = float(input('Informe o salário: R$ '))
bonus = float(input('Informe o bônus: '))
print('-' * 12)
print(f'Seu salário com o bônus de {bonus:.0f}% é: {salario + (salario*bonus/100)}')