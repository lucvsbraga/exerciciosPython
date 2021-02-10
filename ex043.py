# @author: lucvsbraga

altura = float(input('Altura em metros: '))
peso = float(input('Peso em quilos: '))
print('-' * 12)
imc = peso / (altura ** 2)

print(f'IMC: {imc:.2f}')

if imc < 18.5:
    print('Abaixo do peso.')
elif imc < 25:
    print('Peso ideal.')
elif imc < 30:
    print('Sobrepeso.')
elif imc < 40:
    print('Obeso')
else:
    print('Obeso mórbido.')
