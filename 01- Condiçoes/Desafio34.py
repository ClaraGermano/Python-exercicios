#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.Para
#salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

'''salario = float(input('Qual o salário do funcionário? R$'))

if salario > 1250:
    aumento = (salario * 10)/100
    novo = aumento + salario
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(salario, novo))

if salario <= 1250:
    aumento = (salario * 15)/100
    novo = aumento + salario
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(salario,novo))'''


salario = float(input('Qual o salário do funcionario?R$'))

if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)

print('Quem recebia \033[34mR${:.2f}\033[m, vai passar a receber \033[31mR${:.2f}\033[m'.format(salario,novo))





