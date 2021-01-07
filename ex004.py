# @author: lucvsbraga

entrada = input('Digite algo: ')
print('O dado digitado é do tipo:', type(entrada))  # TIPO DA VARIÁVEL
# RETORNA TRUE SE A STRING CONTER APENAS ESPAÇOS
print('Contém apenas espaços:', entrada.isspace())
# RETORNA TRUE SE O DADO FOR NUMÉRICO
print('É um número:', entrada.isnumeric())
# RETORNA TRUE SE O DADO FOR ALFABÉTICO
print('É alfabético:', entrada.isalpha())
# RETORNA TRUE SE O DADO FOR ALFANUMÉRICO
print('É alfanumérico:', entrada.isalnum())
# RETORNA TRUE SE O DADO ESTIVER EM CAPSLOCK
print('Contém apenas letras maiúsculas:', entrada.isupper())
# RETORNA TRUE SE O CONTER APENAS LETRAS MINÚSCULAS
print('Contém apenas letras minúsculas:', entrada.islower())
# RETORNA TRUE SE ESTIVER 'Capitalizado'
print('Está capitalizada:', entrada.istitle())
