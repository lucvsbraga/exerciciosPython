from random import sample
from time import sleep

qtdJogos = int(input('Quantidade de jogos: '))
print()

for i in range(qtdJogos):
    print(sorted(sample(range(0, 60), 6)))
    sleep(0.45)