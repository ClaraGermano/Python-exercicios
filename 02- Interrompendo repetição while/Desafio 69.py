# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.


continuar = ' '
maior_idade = 0
sexo_masc = 0
idade_mulher = 0

while True:
    print('\033[34m-=-\033[m'*10)
    print('\033[33m  CADASTRE UMA PESSOA ⌨️\033[m')
    print('\033[34m-=-\033[m'*10)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo[F/M]: ')).strip().upper()[0]

    if idade > 18:
        maior_idade += 1
    if sexo == 'M':
        sexo_masc += 1

    if sexo == 'F':
        if idade < 20:
            idade_mulher += 1

    continuar = ' '   # reinicia para forçar a validação toda vez
    while continuar not in 'SN':
        continuar = str(input('Quer continuar[S/N]? ')).strip().upper()[0]

    if continuar == 'N':
        break

print('\033[31m-*-\033[m'*15)

print(f'Total de pessoas com mais de 18 anos: {maior_idade}')
print(f'Total Homens cadastrados: {sexo_masc}')
print(f'Total mulheres com menos de 20 anos: {idade_mulher} ')
