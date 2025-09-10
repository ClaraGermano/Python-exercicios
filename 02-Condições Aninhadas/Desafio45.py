#Crie um programa que faça o computador jogar Jokenpô com você.

print('\033[34m -*- \033[m'*8)
print('\033[31m    Vamos jogar Jokenpô \033[m')
print('\033[34m -*- \033[m'*8)

#computador
from random import randint
from time import sleep
lista = ['Pedra' , 'Papel' , 'Tesoura']
computador = randint(0,2)


#jogador
print('Suas opções:')
print('[ 0 ] Pedra')
print('[ 1 ] Papel')
print('[ 2 ] Tesoura')
jogador = int(input('Qual é sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')

print('\033[1;31m-=\033[m'*13)
print('O Computador jogou {}'.format(lista[computador]))
print('O Jogador jogou {}'.format(lista[jogador]))
print('\033[1;31m-=\033[m'*13)

if computador == 0:   #computador jogou pedra
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('Você GANHOU!')
    elif jogador == 2:
        print('Você PERDEU!')
    else:
        print('Opção inválida. Tente novamente!')
elif computador == 1:    #computador jogou papel
    if jogador == 0:
        print('Você PERDEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('Você GANHOU!')
    else:
        print('Opção inválida. Tente Novamente!')
elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('Você GANHOU!')
    elif jogador == 1:
        print('Você PERDEU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Opção inválida. Tente Novamente!')



