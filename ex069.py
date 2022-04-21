# @author: lucvsbraga
import os
h = 0
m20 = 0
adulto = 0
while True:
    os.system('cls')
    print('C A D A S T R O   D E   P E S S O A S')
    idade = int(input('Idade: '))
    sexo = input('Sexo (F/M): ')
    if idade > 18:
        adulto += 1
    if sexo in 'Mm':
        h += 1
    elif sexo in 'Ff' and idade < 20:
        m20 += 1

    opcao = input('Deseja continuar? (S/N): ')
    if opcao in 'Nn':
        os.system('cls')
        break


print(f'Adultos: {h}')
print(f'Homens: {h}')
print(f'Mulheres com menos de 20: {m20}')
    
