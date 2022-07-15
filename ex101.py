
def vota(nascimento):
  from datetime import date
  today = date.today()
  idade = today.year - nascimento
  if idade < 16:
    print(f'{idade} anos - Não vota!')
  elif idade >= 16 and idade < 65:
    print(f'{idade} anos - Voto obrigatório!')
  else:
    print(f'{idade} anos - Voto facultativo!')

nascimento = int(input('Digite a data de nascimento: '))
vota(nascimento)