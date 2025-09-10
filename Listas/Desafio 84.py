#Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.


dado = list()
lista = list()
cont = 0
maiorpeso = 0
menorpeso = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    lista.append(dado[:])                        #cópia
    cont += +1

    if cont == 1:
        maiorpeso = dado[1]
        menorpeso = dado[1]
    else:
        if dado[1] > maiorpeso:
            maiorpeso = dado[1]
        if dado[1] < menorpeso:
            menorpeso = dado[1]

    dado.clear()                                 #apagando


    usuario = ' '
    while usuario not in 'SN':
        usuario = str(input('Quer continuar[S/N]?: ')).strip().upper()[0]

    if usuario == 'N':
        break

print('\033[31m=-=\033[m'*30)
print(f'Ao todo você cadastrou {cont} pessoas !')

print(f'O maior peso foi {maiorpeso}kg. Peso de: ',end='')
for p in lista:
    if p[1] == maiorpeso:
        print(f'[{p[0]}]' ,end='')
print(f'\nO menor peso foi {menorpeso}kg. Peso de:',end='')
for p in lista:
    if p[1] == menorpeso:
        print(f'[{p[0]}]' ,end='')

#Obs: ao inves do contador para ver quantas pessoas foram cadastradas, podemos colocar:
#print(f'Foram cadastradas {len(lista)}') vai ler quantas direto da lista principal