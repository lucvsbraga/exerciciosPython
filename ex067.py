# @author: lucvsbraga
opcao = 1

while opcao > 0:
    n = int(input('Número: '))
    for i in range(1, 11, 1):
        print(f'{n} x {i} = {n * i}')
    
    opcao = int(input('Continua?: '))