# @author: lucvsbraga
import os
times = ('São Paulo','Internacional','Atlético-MG','Flamengo','Palmeiras','Grêmio','Fluminense','Santos','Corinthians','Atlético-PR','Ceará','Atlético-GO','Bragantino','Sport','Bahia','Vasco','Fortaleza','Goiás','Coritiba','Botafogo')

os.system('clear')
print(f'Top 5: {times[0:5]}')
print('-' * 12)
print(f'Ordem alfabética: {sorted(times)}')
print('-' * 12)
print(f'O Flamengo está na {times.index("Flamengo")+1}ª posição.')