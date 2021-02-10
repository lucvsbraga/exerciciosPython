# @author: lucvsbraga

valor = int(input('Informe o valor a ser sacado : '))
nota50 = valor // 50
valor %=  50
nota20 = valor // 20
valor %= 20
nota10 = valor // 10
valor %= 10
nota5 = valor // 5
valor %= 5
nota2 = valor // 2
valor %= 2
nota1 = valor // 1
print(f'Cédulas de 50 = {nota50}')
print(f'Cédulas de 20 = {nota20}')
print(f'Cédulas de 10 = {nota10}')
print(f'Cédulas de 5 = {nota5}')
print(f'Cédulas de 2 = {nota2}')
print(f'Cédulas de 1 = {nota1}')