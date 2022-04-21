import os

jogador = {}
jogador['nome'] = input('Nome do jogador: ')
jogador['qtdJogos'] = int(input('Quantidade de jogos: '))
jogador['qtdGols'] =  []

for i in range(0, jogador['qtdJogos']):
  jogador['qtdGols'].append(int(input(f'Número de gols na partida {i+1}: ')))

os.system('cls')
print('*' * 30)
print(f'O {jogador["nome"]} jogou {jogador["qtdJogos"]} partidas.') 
print('Números de gols marcados por ' + jogador['nome'] + ': ')

for i in range(0, jogador['qtdJogos']):
  print(f'Gols marcados na partida {i+1}: ',  jogador['qtdGols'][i])

print(f'Total de gols no campeonato: ', sum(jogador['qtdGols']))