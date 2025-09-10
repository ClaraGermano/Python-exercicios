# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja
# errado, peça a digitação novamente até ter um valor correto.


'''sexo = str(input('Informe seu sexo:')).strip().upper()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Erro! Dados inválidos. Informe seu sexo:')).strip().upper()

print('Sexo {} registrado com sucesso!'.format(sexo))'''


# jeito professor

sexo = str(input('Informe seu sexo:')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Informe seu sexo:')).strip().upper()[0]

print('Sexo {} registrado com sucesso!'.format(sexo))

