# @author: lucvsbraga

cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
        'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')


while True:
    num = int(input('Digite um número entre 0 e 20: '))
    
    while num < 0 or num > 20:
        num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
        
    print(f'Você digitou o número {cont[num]}')
    resposta = input('Você quer continuar? [S/N]: ').upper()
    
    if resposta in 'Ss':
        continue
    else:
        break

