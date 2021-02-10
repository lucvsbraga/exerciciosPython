# @author: lucvsbraga

from time import sleep

contagem = int(input('Contagem: '))
print('-' * 12)

for i in range(contagem):
    print(contagem - i)
    sleep(1)


print('\n\nA contagem chegou ao fim.')
