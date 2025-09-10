#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
#separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista = list()
par = list()
impar = list()

for n in range(1,8):
    lista.append(int(input(f'Digite o {n}° valor: ')))

for n in lista:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

print('\033[31m=-=\033[m'*30)
par.sort()
impar.sort()
print(f'Os valores pares digitados foram {par}')
print(f'Os valores ímpares digitados foram {impar}')
