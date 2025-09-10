#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

'''import math
a = float(input('Digite o ângulo que você deseja:'))
s = math.sin(math.radians(a))
print('O ângulo de {} , tem o SENO de {:.2f}'.format(a,s))
c = math.cos(math.radians(a))
print('O ângulo de {}, tem o COSSENO de {:.2f}'.format(a,c))
t = math.tan(math.radians(a))
print('O ângulo de {}, tem a tangente de {:.2f}'.format(a,t))'''

from math import sin,tan,cos,radians
angulo = float(input('Digite o ângulo que você deseja:'))
seno = sin(radians(angulo))
print('O ângulo de {} tem o Seno de {:.2f}'.format(angulo,seno))
cosseno = cos(radians(angulo))
print('O ângulo de {} tem o Cosseno de {:.2f}'.format(angulo,cosseno))
tangente = tan(radians(angulo))
print('O ângulo de {} tem a Tangente de {:.2f}'.format(angulo,tangente))


