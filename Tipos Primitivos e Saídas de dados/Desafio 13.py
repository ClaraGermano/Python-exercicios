#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

s = float(input('Qual o salário do funcionário? R$'))
novo = s + (s * 15 / 100)
print('O salário do funcionário que era R${:.2f}, com 15% de aumento passou a ser R${:.2f}'.format(s,novo))
