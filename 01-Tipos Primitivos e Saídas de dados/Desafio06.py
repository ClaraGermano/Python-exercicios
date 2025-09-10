#06:Crie um algoritmo que leia um número e mostre o seu dobro,triplo e raiz quadrada.

n = int(input('Digite um número real:'))
d = n*2
t = n*3
r = n**(1/2)
print('O número escolhido é {}\nO dobro dele é {}, o triplo é {}, e sua raiz é {:.2f}'.format(n,d,t,r))
#  raiz tbm pode ser feita como pow(n,(1/2))


