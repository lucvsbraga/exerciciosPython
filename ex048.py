# @author: lucvsbraga

soma = 0
contador = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma = soma + i
        contador += 1

print(f'Soma: {soma}')
print(f'Valores: {contador}')
