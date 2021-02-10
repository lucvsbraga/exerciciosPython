# @author: lucvsbraga

print('Sequência de toma to...FIBONACCI')
print('-' * 12)

n = int(input('Quantos termos deseja ver? '))

t1 = 0
t2 = 1
i = 0
while i < n:
    t3 = t2 + t1
    print(t3, end='=>')
    i += 1
    t1 = t2
    t2 = t3