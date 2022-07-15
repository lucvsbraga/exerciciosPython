def ficha(jogador = '<desconhecido>', gol = 0):
  print(f'O jogador {jogador} fez {gol} gol(s) no campeonato.')

nome = input('Nome do jogador: ')
gol = input('Número de Gols: ')

if gol.isnumeric():
  gol = int(gol)
else:
  gol = 0
if nome.strip() == '':
  ficha(gol = gol)
else:
  ficha(nome, gol)