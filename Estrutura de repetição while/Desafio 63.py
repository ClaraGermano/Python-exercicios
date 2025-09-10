# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma
# Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

print('\033[1;31m=_=_=_=_=_=_=_=_=_=_=_=_=_=\033[m')
print('  Sequência de Fibonacci')
print('\033[1;31m=_=_=_=_=_=_=_=_=_=_=_=_=_=\033[m')

n1 = 0
n2 = 1
cont = 1
termo = int(input('Quantos termos você quer mostrar?:'))
print('\033[33m~\033[m'*60)

while cont <= termo:
    print('{} -> '.format(n1), end='')
    prox = n1 + n2
    n1 = n2
    n2 = prox
    cont = cont + 1

print('Fim')
print('\033[33m~\033[m'*60)