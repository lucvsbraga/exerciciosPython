# @author: lucvsbraga

p = int(input('Primeiro termo: '))
r = int(int(input('Razão: ')))
t = 9
i = 0
print('-' * 12)
print(p, end=' => ')
while i < t:
    p += r
    print(p, end=' => ')
    i += 1
print('FIM')
