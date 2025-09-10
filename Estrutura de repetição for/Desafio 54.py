# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
# ainda não atingiram a maioridade e quantas já são maiores.


from datetime import date
maior = 0
menor = 0
ano_atual = date.today().year
for c in range(1,8):
    nasc = int(input('Em que ano a {}° pessoa nasceu?'.format(c)))
    idade = ano_atual - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('Tivemos {} pessoas maiores de idade'.format(maior))
print('E tivemos {} menores de idade'.format(menor))





## Tratando singular/plural, se quiser
'''if maior == 1:
    print('Tivemos 1 pessoa maior de idade.')
else:
    print(f'Tivemos {maior} pessoas maiores de idade.')

if menor == 1:
    print('E tivemos 1 pessoa menor de idade.')
else:
    print(f'E tivemos {menor} pessoas menores de idade.')'''



