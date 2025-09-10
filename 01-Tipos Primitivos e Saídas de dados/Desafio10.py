#10:Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar. Considere US1.00 = R$5.56

c = float(input('Quantos Reais você tem na carteira? R$'))
print('Com R$ {:.2f}, você pode comprar US${:.2f}'.format(c,(c/5.56)))











