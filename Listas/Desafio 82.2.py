#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas
# extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

valor = list()

while True:
    valor.append(int(input('Digite um valor: ')))

    usuario = ' '
    while usuario not in 'SN':
        usuario = str(input('Quer continuar[S/N]: ')).strip().upper()[0]
    if usuario == 'N':
        break

par = list()
impar = list()

for v in valor:
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)

print('\033[1;35m=-=\033[m'*30)
print(f'A lista completa é {valor}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')