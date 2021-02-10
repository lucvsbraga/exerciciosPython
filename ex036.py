# @author: lucvsbraga

casa = float(input('Valor da casa: '))
salario = float(input('Salário: '))
tempo = float(input('Tempo de devoução: ')) * 12

prestacao = casa / tempo
if prestacao > (salario * 30 / 100):
    print('Empréstimo não aprovado. As prestações não são compatíveis com o orçamento informado.')
    print(f'Prestação: {prestacao:.2f}')
else:
    print('Empréstimo aprovado.')
    print(f'Prestação: {prestacao:.2f}')
    print(f'Anos: {tempo}')
