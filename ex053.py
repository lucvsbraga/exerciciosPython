# @author: lucvsbraga

p = (input('Digite uma palavra: '))

r = p[::-1]

if p.replace(" ", "").upper() == r.replace(" ", "").upper():
    print(f'{p} = {r}, portanto é um PALÍNDROMO')
else:
    print(f'{p} =/= {r}, portanto NÃO É PALÍNDROMO')
