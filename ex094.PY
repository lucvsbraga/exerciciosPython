pessoa = {}
galera = list()
soma = media = 0
while True:
  pessoa.clear()
  pessoa['nome'] = str(input('Nome: '))
  while True:
    pessoa['sexo'] = str(input('Sexo (M/F): ')).upper()[0]
    if pessoa['sexo'] in 'MF':
      break
    print('Erro! Por favor, digite apenas M ou F.')
  pessoa['idade'] = int(input('Idade: '))
  soma += pessoa['idade']
  galera.append(pessoa.copy())
  while True:
    resposta = str(input('Quer continuar? (S/N): ')).upper()[0]
    if resposta in 'SN':
      break
    print('Erro! Responda apenas S ou N.')
  if resposta == 'N':
    break

print('*' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos.')
print(f'As mulheres cadastradas foram: ', end="")
for p in galera:
  if p['sexo'] == 'F':
    print(f'{p["nome"]} ', end="")
print()

print(f'Lista das pessoas que estão acima da média: ', end="")
for p in galera:
  if p['idade'] > media:
    print(f'{p["nome"]} com {p["idade"]} anos.', end="")
    
print(f'Lista das pessoas que estão abaixo da média: ', end="")
for p in galera:
  if (p["idade"]) < media:
    print(f'{p["nome"]} com {p["idade"]} anos.' , end="")


