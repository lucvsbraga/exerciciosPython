# @author: lucvsbraga 
n = []
n.append(int(input('Digite um número (0 para sair): ')))
print('-' * 12)

while n[-1] != 0:
    print(f'Soma: {sum(n)}')
    n.append(int(input('Digite um número (0 para sair): ')))
    print('-' * 12)

print(f'Você digitou {len(n)} números e a soma é {sum(n)}.')