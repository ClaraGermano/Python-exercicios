# Refazer com outras cedulás, para fixar aprendizado
# OBS:considere que o caixa possui cédulas de R$100, R$50, R$20, R$10, R$5, R$1.


print('\033[33m=\033[m'*20)
print('\033[31m  BANCO CLAJU 💰\033[m')
print('\033[33m=\033[m'*20)

valor_saque = int(input('Quanto você quer sacar?R$ '))

ced = 100
total_ced = 0

while True:
    if valor_saque >= ced:
        valor_saque = valor_saque - ced
        total_ced += 1

    else:
        if total_ced > 0:
            print(f'Total de {total_ced} de R${ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        total_ced = 0
        if valor_saque == 0:
            break

print('\033[33m-\033[m'*30)
print('Obrigada.Volte sempre!')