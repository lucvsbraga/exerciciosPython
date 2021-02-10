# @author: lucvsbraga

n = int(input('Digite um número: '))
print('-' * 12)
print('1 - BINÁRIO')
print('2 - OCTAL')
print('3 - HEXADECIMAL')
opcao = int(input('Escoha a opção: '))
print('-' * 12)

if opcao == 1:
    print(f'Binário: {bin(n)[2:]}')
elif opcao == 2:
    print(f'Octal: {oct(n)[2:]}')
elif opcao == 3:
    print(f'Hexadecimal: {hex(n)[2:]}')
else:
    print(f'Opção Inválida.')
