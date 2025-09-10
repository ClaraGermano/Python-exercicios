#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
#o salário do comprador e em quantos anos ele vai pagar.A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado

print('\033[33m -*- \033[m' *10)
print('\033[1;31m Empréstimo Bancário \033[m')
print('\033[33m -*- \033[m' *10)

casa = float(input('Qual o valor da casa?R$'))
salario = float(input('Qual o valor do seu salário?R$'))
anos = float(input('Em quantos anos pretende pagar?'))
prestação = casa / (anos * 12)

if prestação <= (salario * 30) / 100 :
    print('Para pagar uma casa de R${:.2f} em {:.0f} anos a pretação será de R${:.2f}'.format(casa,anos,prestação))
    print('\033[4;34m Empréstimo aprovado!! \033[m')
else:
    print('Para pagar uma casa de R${:.2f} em {:.0f} anos a prestação será de R${:.2f}'.format(casa,anos,prestação))
    print('\033[4;31m Empréstimo negado! \033[m')


