# @author: lucvsbraga

'''
Escreva um programa que pergunte o salário do funciońario e dê um algumento de 15% caso seu salário
seja menor ou igual à 1250 e 10% caso seja maior.
'''

salario = float(input('Salário: '))
print('-' * 12)

if salario <= 1250:
    print(
        f'Salário atual com bônus de 15%: {salario + (salario * 15 / 100):.2f}')
else:
    print(
        f'Salário atual com bônus de 10%: {salario + (salario * 10 / 100):.2f}')
