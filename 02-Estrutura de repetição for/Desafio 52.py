# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número:'))
cont = 0

for c in range (1 ,n + 1):
    if n % c == 0:
        print('\033[31m', end=' ')
        cont = cont + 1
    else:
        print('\033[37m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(n,cont))

if cont == 2:
    print('Por isso ele \033[33mé PRIMO!\033[m')
else:
    print('Por isso ele \033[33mNÃO É PRIMO!\033[m')









