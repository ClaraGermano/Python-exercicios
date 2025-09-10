#Faça um programa que leia o nome completo de uma pessoa,
#mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Qual seu nome completo?')).strip()
separa = nome.split()
print('Prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(separa[0]))
print('Seu ultimo nome é {}'.format(separa[-1]))


