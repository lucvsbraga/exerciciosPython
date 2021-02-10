# @author: lucvsbraga

sexo = input('Sexo(F/M): ')

while sexo not in 'FfMm':
    print('Dados inválidos.')
    sexo = input('Sexo(F/M): ')

print('-' * 12)
print('Informação atualizada.')
