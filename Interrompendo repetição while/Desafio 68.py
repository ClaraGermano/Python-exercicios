# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador
# perder,mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

# codigo com meu jeito

print('\033[1;33m-_-\033[m'*12)
print('\033[34m  VAMOS JOGAR PAR ou ÍMPAR\033[m')
print('\033[1;33m-_-\033[m'*12)


from random import randint

valor_extenso = ''
valor = ''
cont = 0

while True:
    computador = randint(0,10)
    jogador = int(input('Diga um valor:'))
    soma = computador + jogador


    opcao = ' '
    while opcao not in 'PI':
        opcao = str(input('Par ou Ímpar[P/I] ?: ')).strip().upper()
    print('\033[33m-*-\033[m'*30)

    if soma % 2 == 0:
        valor = 'P'
        valor_extenso = 'PAR'
    else:
        valor = 'I'
        valor_extenso = 'ÍMPAR'
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma}, deu {valor_extenso}')

    if opcao == valor:
        print('Você venceu!')
        print('Vamos jogar novamente...')
        cont += 1

    else:
        break

    print('\033[33m-*-\033[m'*30)

print(f'\033[34mGAME OVER! Você venceu {cont} vez !\033[m')