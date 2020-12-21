# @author: lucvsbraga

'''
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações 
possíveis sobre ele.
'''

entrada = input('Digite algo: ')
print('O dado digitado é do tipo:', type(entrada)) # TIPO DA VARIÁVEL
print('Contém apenas espaços:', entrada.isspace()) # RETORNA TRUE SE A STRING CONTER APENAS ESPAÇOS
print('É um número:', entrada.isnumeric()) # RETORNA TRUE SE O DADO FOR NUMÉRICO
print('É alfabético:', entrada.isalpha()) # RETORNA TRUE SE O DADO FOR ALFABÉTICO
print('É alfanumérico:', entrada.isalnum()) # RETORNA TRUE SE O DADO FOR ALFANUMÉRICO
print('Contém apenas letras maiúsculas:', entrada.isupper()) # RETORNA TRUE SE O DADO ESTIVER EM CAPSLOCK
print('Contém apenas letras minúsculas:', entrada.islower()) # RETORNA TRUE SE O CONTER APENAS LETRAS MINÚSCULAS
print('Está capitalizada:', entrada.istitle()) # RETORNA TRUE SE ESTIVER 'Capitalizado'
