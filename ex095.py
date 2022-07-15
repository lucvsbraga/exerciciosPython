import os

time = list()
jogador = {}
partidas = list()

while True:
  jogador['nome'] = input('Nome do Jogador: ')
  total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
  partidas.clear()
  for c in range(0, total):
    partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
  jogador['gols'] = partidas[:]
  jogador['total'] = sum(partidas)
  time.append(jogador.copy())
  while True:
    resposta = str(input(f'Quer continuar? [S/N]: ')).upper()[0]
    if resposta in 'SN':
      break
    print('Erro! Responda apenas S ou N. ')
  if resposta == 'N':
    break

os.system('cls')
for i in jogador.keys():
  print(f'{i:<15}', end='')
print('')
for k, v in enumerate(time):
  print(f'{k:>3} - ', end='')
  for d in v.values():
    print(f'{str(d):<15}', end= '')
  print()

while True:
  busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
  if busca == 999:
    break
  if busca >= len(time):
    print(f'Erro! Não existe jogador com código da {busca}!')
  else:
    print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
    for i, g in enumerate(time[busca]["gols"]):
      print(f'   No jogo {i+1} fez {g} gols.')
