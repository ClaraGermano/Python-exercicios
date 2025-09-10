#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora
#o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.


from random import randint
from time import sleep
computador = randint(0,10)

print('\033[31m-*-\033[m'*20)
print(' \033[1;32m Vou pensar em um número de 0 a 10. Tente adivinhar 😎 \033[m')
print('\033[31m-*_\033[m'*20)

jogador = int(input('Em que número pensei ?'))
print('\033[33m Processando... \033[m')
sleep(1)

cont = 1

while jogador != computador:
        if computador > jogador:
            print('\033[31m Tente novamente, pensei em um número MAIOR 📈 \033[m')
        else:
            print('\033[31m Tente novamente. Pensei em um número MENOR 📉 \033[m')

        jogador = int(input('Tente novamente...Em que número pensei:'))
        print('\033[33m Processando... \033[m')
        sleep(1)
        cont = cont +1

print('\033[1;34m Parabéns! Você venceu! 🎉 \033[m')
print('Foram necessárias {} palpites para vencer 📝'.format(cont))




# forma do Guanabara

'''from random import randint

computador = randint(0, 10)
acertou = False        #acertou = falso. faz o programa rodar a primeira vez 
palpites = 0

print('Estou pensando em um número entre 0 e 10... Tente adivinhar! 🤔')

while not acertou:           #enquanto acertou for falso...
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1

    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente um número MAIOR 📈')
        else:
            print('Menos... tente um número MENOR 📉')

print('🎉 Parabéns! Você acertou com {} tentativa(s).'.format(palpites)'''
