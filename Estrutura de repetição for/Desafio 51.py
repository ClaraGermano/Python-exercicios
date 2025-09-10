# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.



print('\033[32m=\033[m'*25)
print('\033[31m 10  Termos de uma PA \033[m')
print('\033[32m=\033[m'*25)

termo = int(input('O primeiro termo:'))
razao = int(input('A razão:'))

for a in range (1,11):
    s = termo + (a - 1) * razao
    print('{}'.format(s), end = ' -> ')
print('Fim')

