from random import randint

def sorteia(lista):
  for cont in range(0, 5):
    numero = randint(1, 10)
    lista.append(numero)
    print(numero, end=' ')
    
def somapar(lista):
  total = 0
  for i in lista:
    if i % 2 == 0:
      total += i
  print()
  print(f'Total da soma dos pares: {total}')
  
numeros = list()
sorteia(numeros)
somapar(numeros)