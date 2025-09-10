# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
# da progressão usando a estrutura while.

print('\033[33m=-=-=-=-=-=-=-=-=-=-=-=-=\033[m')
print('   Gerador de PA')
print('\033[33m=-=-=-=-=-=-=-=-=-=-=-=-=\033[m')

primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão da PA:'))
cont = 1
termo = primeiro
while cont <= 10:
    print('{}'.format(termo), end=' ')
    print('\033[33m->\033[m ' if cont < 10 else '', end = '')
    termo = termo + razao
    cont = cont + 1

print('\033[32mFIM\033[m')