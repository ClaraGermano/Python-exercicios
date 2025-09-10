#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
#valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


continuar = ''
media = 0
cont = 0
soma = 0
maior = 0
menor = 0
while continuar != 'N':
    n = int(input('Digite um número: '))
    continuar = str(input('\033[33mQuer continuar[S/N]? :\033[m')).strip().upper()
    cont = cont + 1
    soma = soma + n
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n


media = soma /cont
print('\033[34mVocê digitou {} números e a média foi {:.1f}\033[m'.format(cont,media))
print('\033[34mO maior número digitado foi {} e o menor número digitado foi {}\033[m'.format(maior,menor))