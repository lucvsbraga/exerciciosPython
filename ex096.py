import os

def area(largura, comprimento):
  a = largura * comprimento
  print(f'A área de um terreno {largura}x{comprimento} é de {a}m².')

print('Controle de Terrenos')
print('-' * 20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))

os.system('cls')
print('-' * 20)
area(l, c)