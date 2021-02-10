# @author: lucvsbraga

n = []
i = 's'

while i not in 'Nn':
    n.append(int(input('Número: ')))
    i = input('Continua? (S/N): ')
    print('-' * 12)
    
print(f'Números digitados: {len(n)}')
print(f'Média: {sum(n) / len(n)}')
print(f'Máximo: {max(n)}')
print(f'Mínimo: {min(n)}')