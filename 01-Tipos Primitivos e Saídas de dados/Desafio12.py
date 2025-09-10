#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

p = float(input('Digite o valor do produto: R$'))
desconto = p*0.05         #p * 5 / 100
v = p-desconto
print('O produto que custava {},com desconto de 5% vai sair a R${}'.format(p,v))






