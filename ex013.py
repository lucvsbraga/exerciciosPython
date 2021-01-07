# @author: lucvsbraga

salario = float(input('Informe o salário: R$ '))
bonus = float(input('Informe o bônus: '))
print('-' * 12)
print(f'Salário com o bônus de {bonus:.0f}% é: {salario+(salario*bonus/100)}')
