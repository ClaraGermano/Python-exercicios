#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
#qual foi o número escolhido pelo computador.O programa deverá escrever na tela se o usuário venceu ou perdeu.


from random import choice            #from random import randint
from time import sleep                #faz o computador 'dormir', para dar expectativa de que ele está processando
computador = choice([0,1,2,3,4,5])           #escolhido = randint(0,5)        outro cod, faz o computador 'pensar'

print('---'*20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar :)')
print('---'*20)

jogador = int(input('Em que número eu pensei?'))

print('Processando...')
sleep(3)                                    #esperar 3segundos

if jogador == computador:
    print('Parabéns,você venceu!!')
else:
    print('Você perdeu. Pensei no número {} e não no {}!'.format(computador,jogador))



