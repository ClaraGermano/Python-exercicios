# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final
# do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres
# têm menos de 20 anos.


soma_idade = 0
maior_homem = 0
nome_homem_maior = ''
cont_mulher = 0

for c in range(1,5):
    print('----- {}° pessoa -----'.format(c))
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [F/M]:')).strip().upper()

    soma_idade = soma_idade + idade

    if sexo == 'M':
        if idade > maior_homem:
            maior_homem = idade
            nome_homem_maior = nome
    if sexo == 'F':
        if idade < 20:
            cont_mulher += 1

if maior_homem == 0:
    print('Não teve homem no grupo!')
else:
    print('A idade do homem mais velho é {} e seu nome é {}'.format(maior_homem, nome_homem_maior))

if cont_mulher == 1:
    n = 'mulher'
else:
    n = 'mulheres'

media_idade = soma_idade / 4
print('A média da idade do grupo é {:.2f}'.format(media_idade))
print('{} {} do grupo tem menos de 20 anos'.format(cont_mulher,n))




