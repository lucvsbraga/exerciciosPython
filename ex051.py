# @author: lucvsbraga

print('=' * 24)
print('10 TERMOS DE UMA PA')
print('=' * 24)

p = int(input('Primeiro termpo: '))
r = int(input('Razão: '))
print('-' * 12)

print(p, end=' ')
for i in range(9):
    p = p + r
    print(p, end=' ')
