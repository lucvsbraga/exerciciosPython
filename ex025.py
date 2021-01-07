# @author: lucvsbraga

nome = input('Digite seu nome completo: ')

if "Braga" not in nome:
    print('-' * 12)
    print(f'Você não é um membro, {nome}.')
else:
    print('-' * 12)
    print(f'{nome}, você é um membro da realeza.')
