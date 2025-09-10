#08:Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n1 = float(input('Escreva a distância em metros para conversão:'))
c = n1*100
m = n1*1000
print('O valor em Centimetros é {}cm. \nvalor em Milímetros é {}mm'.format(c, m))
print('Valor em Quilômetro {}km'.format((n1/1000)))



