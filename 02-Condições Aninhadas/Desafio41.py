# A Confederação Nacional de Natação precisa de um programa
#que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JÚNIOR
#Até 25 anos: SÊNIOR
#Acima de 25 anos: MASTER


from datetime import date
ano_atual = date.today().year

nasc = int(input('Ano de nascimento:'))
idade = ano_atual - nasc

print('O atleta tem {} anos'.format(idade))

if idade <= 9:
    print('Categoria: Mirim')
elif 9 < idade <= 14:
    print('Categoria: Infantil')
elif  idade <= 19:
    print('Categoria: Júnior')
elif  idade <= 25:
    print('Categoria: Sênior')
elif idade > 25:
    print('Categoria: Master')


