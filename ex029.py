# @author: lucvsbraga

velocidade = int(input('Velocidade atual: '))
print('-' * 12)

if velocidade <= 80:
    print('Mantenha sempre no limite.')
else:
    print(f'Você foi multado em {(velocidade - 80) * 7} reais.')
