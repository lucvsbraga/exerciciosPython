# @author: lucvsbraga

salario = float(input('Salário: '))
print('-' * 12)

if salario <= 1250:
    print(
        f'Salário atual com bônus de 15%: {salario + (salario * 15 / 100):.2f}')
else:
    print(
        f'Salário atual com bônus de 10%: {salario + (salario * 10 / 100):.2f}')
