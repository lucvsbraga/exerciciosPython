# author: lucvsbraga

vogais = ('a', 'e', 'i', 'o', 'u')
palavra = input('Digite uma palavra: ')


print(f'Vogais da palavra ({palavra}): ', end='')

for letra in palavra:
    if letra.lower() in vogais:
        print(f'\033[1;33m{letra.lower()}\033[m', end=' ')
print()