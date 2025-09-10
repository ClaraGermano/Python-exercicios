#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.


valor = list()
while True:
    valor.append(int(input('Digite um valor: ')))

    usuario = ' '
    while usuario not in 'SN':
        usuario = str(input('Quer continuar[S/N]?: ')).strip().upper()[0]
    if usuario == 'N':
        break

print('\033[33m=-=\033[m'*30)
valor.sort(reverse=True)
print(f'\033[34mForam digitador {len(valor)} números!\033[m')
print(f'\033[34mA lista de valores ordenada de forma decrescente é: {valor}\033[m')

if 5 in valor:
    print('\033[34mO valor 5 foi encontrado na lista!\033[m')
else:
    print('\033[34mO valor 5 não foi encontrado na lista!\033[m')
