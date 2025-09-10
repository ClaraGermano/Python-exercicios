#Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
#calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

# IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida

print('\033[35m -*- \033[m'*8)
print('  Índice de Massa Corporal (IMC) ')
print('\033[35m -*- \033[m'*8)

peso = float(input('Qual seu peso?(Kg)'))
altura = float(input('Qual sua altura?(m)'))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Seu IMC é {:.2f} : \033[33m Abaixo do Peso \033[m'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é {:.2f} : \033[34m Peso Ideal \033[m'.format(imc))
elif 25 <= imc < 30:
    print('Seu imc é {:.2f} : \033[33m Sobrepeso \033[m'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é {:.2f} : \033[31m Obesidade \033[m'.format(imc))
else:
    print('Seu IMC é {:.2f} : \033[31m Obesidade Mórbida.Cuidado! \033[m'.format(imc))


