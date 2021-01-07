# @author: lucvsbraga

dias = int(input('Digite o número de dias com o carro alugado: '))
km = float(input('Digite a quantidade de km percorridos: '))
print('-' * 12)
total = (dias * 60) + (km * 0.15)
print(f'Total a pagar: R$ {total:.2f}')
