#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário
#vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.


print('\033[33m**\033[m'*15)
print('\033[31m  LOJA SUPER BARATÃO\033[m')
print('\033[33m**\033[m'*15)

cont = 0
menor = 0
total = 0
cont_valor = 0
barato = ' '

while True:
    produto = str(input('Nome do produto: ')).strip()
    valor = float(input('Preço do produto:R$ '))

    total = total + valor
    cont += 1

    if valor > 1000:
        cont_valor += 1

    if cont == 1 or valor < menor: #    # Registra o primeiro produto ou atualiza o mais barato
        menor = valor
        barato = produto

    usuario = ' '
    while usuario not in 'SN':         # Pergunta se continua
        usuario = str(input('Quer continuar[S/N]?: ')).strip().upper()[0]
    if usuario == 'N':
        break

print('\033[33m-\033[m'*20)
print('\033[1;31m  FIM DO PROGRAMA\033[m')
print('\033[33m-\033[m'*20)

print(f'O valor total da sua compra é {total:.2f}')
print(f'Na sua compra tem {cont_valor} que custam acima de R$1000')
print(f'O produto mais barato é {barato} e custa {menor:.2f}')


