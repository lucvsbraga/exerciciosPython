# @author: lucvsbraga

n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
opcao = 0

while opcao != 6:
    print('=' * 24)
    print('1 - Somar')
    print('2 - Subtrair')
    print('3 - Multiplicar')
    print('4 - Dividir')
    print('5 - Home')
    print('6 - Sair')
    print('=' * 24)

    opcao = int(input('Opção: '))

    if opcao == 1:
        print(f'Soma = {n1 + n2} ')
    elif opcao == 2:
        print(f'Subtração = {n1 - n2} ')
    elif opcao == 3:
        print(f'Multiplicação = {n1 * n2} ')
    elif opcao == 4:
        print(f'Dividir = {n1 / n2} ')
    elif opcao == 5:
        n1 = int(input('Número 1: '))
        n2 = int(input('Número 2: '))
    else:
        print('Opção inválida.')
