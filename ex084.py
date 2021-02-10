# @author: lucvsbraga
temp = []
princ = []
opcao = ''
mai = men = 0

while True:
    temp.append(input('Nome: '))
    temp.append(int(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
            
    princ.append(temp[:])
    temp.clear()
    opcao = input('Deseja continuar? [S/N]: ')
    if opcao in 'Nn':
        break

print(princ)


print(f'Mais pesado: {mai}. Peso de ', end= ' ')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]}', end= ' ')
print()
print(f'Menos pesado: {men}. Peso de ', end= ' ')
for p in princ:
    if p[1] == men:
        print(f'{p[0]}', end= ' ')