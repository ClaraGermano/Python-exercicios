#Elabore um programa que calcule o valor a ser pago por um produto,
#considerando o seu preço normal e condição de pagamento:
#1 à vista dinheiro/cheque: 10% de desconto
#2 à vista no cartão: 5% de desconto
#3 em até 2x no cartão: preço formal
#4 3x ou mais no cartão: 20% de juros

print('{:#^40}'.format('\033[1;34m LOJA CLAJU \033[m'))

preço = float(input('Preço das compras:R$'))
print('Forma de pagamento:')
print('[ 1 ] à vista dinhero/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')

pag = int(input('Qual a opção?'))

if pag == 1:
    novo = preço - (preço * 10 / 100)
elif pag == 2:
    novo = preço - (preço * 5 / 100)
elif pag == 3:
    novo = preço
    parc = preço/2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parc))
elif pag == 4:
    parc = int(input('Quantas parcelas?'))
    novo = preço + (preço * 20 / 100)
    print('Sua compra será parcelada em {}x de R${:.2f} com JUROS'.format(parc,novo/parc))
else:
    novo = preço
    print('\033[31m Opção inválida. Tente novamente! \033[m')
print('Sua compra de R${:.2f}, vai custar R${:.2f}'.format(preço,novo))



