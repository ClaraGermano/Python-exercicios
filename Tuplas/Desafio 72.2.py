# deixando o exercercio 72 melhor

cont = ('zero','um', 'dois', 'três','quatro','cinco','seis','sete','oito','nove',
        'dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    n = int(input('Digite um número entre 0 e 20: '))

    while n < 0 or n > 20:
        n = int(input('\033[31mDigite um número válido!\033[m\nDigite um número entre 0 e 20: '))
    print(f'Você digitou o número \033[31m{cont[n]}\033[m')

    usuario = ' '
    while usuario not in 'NS':
        usuario = str(input('Quer continuar[S/N]? ')).strip().upper()[0]

    if usuario == 'N':
        break

print('\033[1;33mFim do Programa!\033[m')
