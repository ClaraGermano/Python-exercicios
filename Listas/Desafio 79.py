#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número
#já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valor = list()
cont = 0
while True:
    v = int(input('Digite um valor: '))
    cont = cont + 1

    if cont == 1:
        valor.append(v)
        print('\033[34mValor adicionado!!\033[m')

    else:
        if v not in valor:
            valor.append(v)
            print('\033[34mValor adicionado com sucesso!\033[m')
        else:
            print('\033[31mValor já axiste na lista! Não adionado!\033[m')

    usuario = ' '
    while usuario not in 'NS':
        usuario = str(input('\033[33mQuer continuar?[S/N]: \033[m')).upper().strip()[0]

    if usuario == 'N':
        break

valor.sort()
print('\033[34m=-=\033[m'*25)
print(f'Você digitou os valores: {valor}')


