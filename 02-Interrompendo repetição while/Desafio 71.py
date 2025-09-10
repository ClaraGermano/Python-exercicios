# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte
# ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
# cédulas de cada valor serão entregues.
# OBS:considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('\033[33m=\033[m'*20)
print('\033[31m  BANCO CLAJU 💰\033[m')
print('\033[33m=\033[m'*20)

valor_saque = int(input('Que valor você quer sacar?R$ '))
ced = 50
tot_ced = 0

while True:
    if valor_saque >= ced:
        valor_saque = valor_saque - ced
        tot_ced += 1

    else:
        if tot_ced > 0:
            print(f'Total de {tot_ced} de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        tot_ced = 0
        if valor_saque == 0:
            break

print('\033[33m-\033[m'*30)
print('Obrigada! Volte sempre!! ')


