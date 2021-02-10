# @author: lucvsbraga

num_1 = float(input('Digite o primeiro número: '))
num_2 = float(input('Digite o segundo número: '))
print('-' * 12)

if num_1 == num_2:
    print('Os números são iguais.')
elif num_1 > num_2:
    print('O primeiro número é maior.')
else:
    print('O segundo número é maior.')
