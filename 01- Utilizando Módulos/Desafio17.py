#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

'''from math import sqrt
co = float(input('Qual o comprimento do Cateto Oposto? '))
ca = float(input('Qual o comprimento do Cateto Adjacente?'))
h = sqrt( (co**2) + (ca**2) )
print('O comprimento da hipotenusa é {:.2f}'.format(h))'''

from math import hypot
co = float(input('Valor do Cateto Oposto:'))
ca = float(input('Valor do Cateto Adjacente:'))
hi = hypot(co,ca)
print('O comprimento da Hipotenusa é {:.2f}'.format(hi))




