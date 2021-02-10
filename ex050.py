# @author: lucvsbraga

aux = 0
cont = 0
for i in range(6):
    n = int(input(f'Digite o {i+1}º número: '))
    if n % 2 == 0:
        aux = aux + n
        cont += 1

print(f'-' * 12)
print(f'Números contabilizados: {cont}\nSoma: {aux}')
