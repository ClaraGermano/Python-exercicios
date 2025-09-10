#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.


a = int(input('Primeiro valor:'))
b = int(input('Segundo valor:'))
c = int(input('Terceiro valor:'))

#Testanto menor
menor = a

if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# Testanto maior

maior = a

if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor número é \033[36m{}\033[m'.format(menor))
print('O maior número é \033[32m{}\033[m'.format(maior))

