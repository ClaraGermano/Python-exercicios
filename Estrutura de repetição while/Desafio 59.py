#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
menu = 0

while menu != 5:
    print('\033[1;34m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[m')
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair do programa')
    menu = int(input('>>>>> Qual sua opção ?'))

    if menu == 1:
        soma = n1 + n2
        print('\033[1;33mA soma de {} + {} é {}\033[m'.format(n1,n2,soma))
    elif menu == 2:
        produto = n1*n2
        print('\033[1;33mA multiplicação de {} x {} é {}\033[m'.format(n1,n2,produto))
    elif menu == 3:
        if n1 > n2:
            print('\033[1;33mO maior número entre {} e {} é {}\033[m'.format(n1,n2,n1))
        elif n2 > n1:
            print('\033[1;33mO maior número entre {} e {} é {}\033[m'.format(n1, n2, n2))
        else:
            print('\033[1;33mOs números são iguais\033[m')
    elif menu == 4:
        print('Informe os números novamente:')
        n1 = int(input('\033[32mPrimeiro valor:\033[m'))
        n2 = int(input('\033[32mSegundo valor:\033[m'))
    elif menu not in range (1,6):
        print('\033[1;31mOpção inválida tente novamente\033[m')

print('Finalizando...⌛')
sleep(2)
print('Fim do Programa. Até a próxima!!☺️')
