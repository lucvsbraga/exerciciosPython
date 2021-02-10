# @author: lucvsbraga
import os

tupla = (int(input('Digite o primeiro valor: ')), int(input('Digite o segundo valor: ')), int(input('Digite o terceiro valor:')), int(input('Digite o quarto valor: ')))

os.system('clear')
print(tupla)
print(f'Número de vezes que o nove aparece: {tupla.count(9)}')

if 3 in tupla:
    print(f'Posição do número 3: {tupla.index(3)}')
else:
    print('O número 3 não aparece.')

print('Pares:', end =' ')   
for i in tupla:
    if i % 2 == 0:
        print(i, end = ' ')