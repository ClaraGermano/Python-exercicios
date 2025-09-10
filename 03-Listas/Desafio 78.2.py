#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o
# menor valor digitado e as suas respectivas posições na lista.


valor = list()
maior = 0
menor = 0

for p in range(0,5):
    valor.append(int(input(f'Digite um valor na posição {p}: ')))
    if p == 0:
        maior = valor[p]
        menor = valor[p]
    else:
        if valor[p] > maior:
            maior = valor[p]

        if valor[p] < menor:
            menor = valor[p]

print('\033[33m=-\033[m'*20)
print(f'Você digitou os valores {valor}')

print(f'O maior valor é {maior} nas posições ',end=' ')

for i,v in enumerate(valor):
    if v == maior:
        print(f'{i}',end='...')

print(f'\nO menor valor é {menor} nas posições',end=' ')

for i,v in enumerate(valor):
    if v == menor:
        print(f'{i}',end='...')






