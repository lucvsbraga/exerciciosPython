ficha = list()
while True:
    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    
    ficha.append([nome, [n1, n2], media])
    
    opcao = input('Deseja continuar? [S/N]:')
    if opcao in 'Nn':
        break
    
print(ficha)