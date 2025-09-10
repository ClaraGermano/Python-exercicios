#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda
#vai se alistar ao serviço militar,se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.


from datetime import date       #importando para ano atual
nasc = int(input('Ano de nascimento:'))
ano_atual = date.today().year      #ano atual
idade = ano_atual - nasc              #idade

print('Quem nasceu em {} tem {} em {}'.format(nasc,idade,ano_atual))

if idade == 18:
    print('Deve se alistar IMEDIANTAMENTE!')
elif idade < 18:
    saldo = 18 - idade                    #quantos anos faltam para alistamento
    print(' Faltam {} anos para seu alistamento'.format(saldo))
    print('Seu alistamento será em {}'.format(ano_atual + saldo))      #ano que vai se alistar
elif idade > 18:
    saldo = idade - 18                     #quanto anos passou do alistamento
    print('Deveria ter se alistado há {} anos'.format(saldo))
    print('Seu alistamento foi em {}'.format(ano_atual - saldo))    #ano deveria ter se alistado







