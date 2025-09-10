#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais


a = int(input('Primeiro número inteiro:'))
b = int(input('Segundo número inteiro:'))

if a > b:
    print('\033[1;36m O PRIMEIRO número é maior! \033[m')
elif b > a:
    print('\033[1;36m O SEGUNDO número é maior! \033[m')
else:
    print('\033[1;36m Os dois números são IGUAIS! \033[m')
