#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas
# extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.


valor = list()
par = list()
impar = list()
while True:
    n = int(input('Digite um valor: '))
    valor.append(n)

    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

    usuario = ' '
    while usuario not in 'SN':
        usuario = str(input('\033[33mQuer continuar[S/N]: \033[m')).strip().upper()[0]

    if usuario == 'N':
        break

print('\033[1;35m=-=\033[m'*30)
print(f'A lista completa é {valor}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')