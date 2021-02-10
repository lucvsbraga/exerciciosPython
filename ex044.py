# @author: lucvsbraga

print('=' * 12 + 'Especiarias' + '=' * 12)
compras = float(input('Total das compras: '))

print('-' * 12)
print('1 - À vista no dinheiro/cheque.')
print('2 - À vista no cartão.')
print('3 - 2x no cartão.')
print('4 - 3x ou mais no cartão.')

opcao = int(input('Opção de pagamento: '))
print('-' * 12)

if opcao == 1:
    compras = compras - (compras * 10 / 100)
elif opcao == 2:
    compras = compras - (compras * 5 / 100)
elif opcao == 3:
    print(f'Duas parcelas de: R${compras/2:.2f}')
elif opcao == 4:
    parcelas = int(input('Número de parcelas: '))
    compras = compras + (compras * 20 / 100)
    print(f'Compra feita em {parcelas} parcelas de R${compras/parcelas:.2f}.')
else:
    print('Tente novamente mais tarde.')

print(f'Total: R${compras:.2f}')
