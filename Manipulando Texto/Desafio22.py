# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
#  Quantas letras tem o primeiro nome.


nome = str(input('Qual o seu nome completo?')).strip()    #strip elimina espaço antes e depois
print('Analisando o seu nome...')
print('Seu nome em Maiúsculo é',nome.upper())
print('Seu nome em Minúsculo é {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))    # lendo o nome - os espaços vazios
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))     #ele procura o primeiro espaço que aparece
#separa = nome.split()
#print(separa)
#print('Seu primeiro nome é {} e tem {}'.format(separa[0], len(separa[0])))









