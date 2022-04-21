# @author: lucvsbraga   

from random import randint
from time import sleep
from operator import itemgetter
import os
ranking = {}
c = 1

jogador = {'Jogador 1': randint(1,6),'Jogador 2': randint(1,6),'Jogador 3': randint(1,6),'Jogador 4': randint(1,6)}

ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)

for k, v in jogador.items():
    print(f'{k} tirou {v}')
    sleep(0.45)

os.system('cls')
print('== RANKING ==')

for i, v in enumerate(ranking):
    print(f'{i+1}º LUGAR:  {v[0]} ---- {v[1]}')
    sleep(0.45)