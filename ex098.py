from time import sleep

def contador(inicio, fim, passo):
  print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
  if passo < 0:
    passo *= -1
  if passo == 0:
    passo = 1
  if inicio < fim:
    cont = inicio
    while cont <= fim:
      print(f'{cont} ', end='')
      sleep(0.2)
      cont += passo
    print('FIM!')
  else:
    cont = inicio
    while cont >= fim:
      print(f'{cont} ', end='')
      sleep(0.2)
      cont -= passo
    print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)
print('Personalize sua contagem.')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)