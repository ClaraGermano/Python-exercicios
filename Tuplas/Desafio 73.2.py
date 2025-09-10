# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Fluminense.

# Jeito mais rápido e fácil, usando fatiamento

times = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Bahia', 'Botafogo',
         'Mirassol', 'São Paulo', 'Fluminense', 'Red Bull Bragantino',
         'Ceará', 'Atlético Mineiro', 'Internacional', 'Grêmio',
         'Corinthians', 'Santos', 'Vasco da Gama', 'Vitória', 'Juventude', 'Fortaleza', 'Sport Recife')

print(f'Lista de Times do Brasileirão: {times}')
print('\033[33m=-=-=\033[m'*40)
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print('\033[33m=-=-=\033[m'*40)
print(f'Os 4 ultimos colocados são: {times[-4:]}')
print('\033[33m=-=-=\033[m'*40)
print(f'Os times em ordem alfabética: {sorted(times)}')
print('\033[33m=-=-=\033[m'*40)
print(f'O fluminense está na posição {times.index("Fluminense")+1}° posição')  #tem que colocar aspas duplas para o python entender a diferença
