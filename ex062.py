# @author: lucvsbraga

print('=' * 12 + ' PA v.3 ' + '=' * 12)

p = int(input('Primeiro termo: '))
r = int(int(input('Razão: ')))
aux = 0


def pa(p, r, it=10, aux=0):
    for i in range(it):
        print(p, end=' => ')
        p += r
        i += 1
    print('FIM')
    print('-' * 12)
    aux += it
    t = int(int(input('Continua: ')))
    print('-' * 12)
    if t == 0:
        print('FIM')
        print(f'Termos: {aux}')
    else:
        pa(p, r, t, aux)


pa(p, r, 10, aux)
