# @author: lucvsbraga

'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex: 
1834
unidade: 4
dezena: 3
centena: 8 
milhar: 1 
'''

n = int(input('Digite um número: '))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

if len(str(n)) == 1:
    print('-' * 12)
    print(f'Unidades: {u}')
elif len(str(n)) > 1 and len(str(n)) < 3:
    print('-' * 12)
    print(f'Dezenas: {d}')
    print(f'Unidades: {u}')
elif len(str(n)) > 2 and len(str(n)) < 4:
    print('-' * 12)
    print(f'Centenas: {c}')
    print(f'Dezenas: {d}')
    print(f'Unidades: {u}')
elif len(str(n)) > 3 and len(str(n)) < 5:
    print('-' * 12)
    print(f'Milhares: {m}')
    print(f'Centenas: {c}')
    print(f'Dezenas: {d}')
    print(f'Unidades: {u}')
else:
    print('Número inválido, tente novamente mais tarde.')


#print(f'Unidades: {u}')
#print(f'Dezenas: {d}')
#print(f'Centenas: {d}')
#print(f'Milhares: {d}')
