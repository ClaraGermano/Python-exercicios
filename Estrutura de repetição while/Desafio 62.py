# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.


primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão da Pa:'))
cont = 1
termo = primeiro
mais = 10
total = 0

while mais != 0:                # Laço externo → controla o programa
    total = total + mais
    while cont <= total:        # Laço interno → imprime os termos
        print('{} -> '.format(termo),end='')
        termo = termo + razao
        cont = cont + 1
    print('Pausa')
    mais = int(input('Quantos termos quer mostrar a mais ?: '))

print('Progressão Finalizada com {} termos mostrados'.format(total))
