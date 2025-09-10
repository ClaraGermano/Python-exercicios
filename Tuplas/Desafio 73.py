# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Fluminense.

times = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Bahia', 'Botafogo',
         'Mirassol', 'São Paulo', 'Fluminense', 'Red Bull Bragantino',
         'Ceará', 'Atlético Mineiro', 'Internacional', 'Grêmio',
         'Corinthians', 'Santos', 'Vasco da Gama', 'Vitória', 'Juventude', 'Fortaleza', 'Sport Recife')

print(f'Lista de Times do Brasileirão: {times}')
print('\033[33m=-=-=\033[m'*40)

# a) Os 5 primeiros times.
print('\033[34mOs 5 primeiros colocados são:\033[m')
for cont in range (0, 5):
    print(f'O {cont+1}° colocado é: {times[cont]}')
print('\033[33m=-=-=\033[m'*40)

# b) Os últimos 4 colocados.
print('\033[34m Os 4 ultimos colocados são:\033[m')
total = len(times)  #20
for cont in range (len(times)-4,total):   #20 - 4 , 20 =  (16,20)
    print(f'O {cont+1}° colocado é: {times[cont]}')
print('\033[33m=-=-=\033[m'*40)

# c) Times em ordem alfabética.
print('\033[34m Times na ordem alfabetica:\033[m')
print(sorted(times))
print('\033[33m=-=-=\033[m'*40)

# d) Em que posição está o time da Fluminense.

for cont in range (len(times)):
    t = times[cont]
    if t == 'Fluminense':
        print(f'O Fluminense está na {cont+1}°')
