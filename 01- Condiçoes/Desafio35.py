#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
#se elas podem ou não formar um triângulo.

print('-*-'*10)
print('Analisador de triângulos')
print('-*-'*10)

a = int(input('Digite o primeiro segmento:'))
b = int(input('Digite o segundo seguimento:'))
c = int(input('Digite o terceiro seguimento:'))

if a + b > c and a + c > b and c + b > a:
    print('Os segmento acima \033[34mFORMAM\033[m um triângulo!')
else:
    print('Os segmentos acima \033[31mNÃO FORMAM\033[m um triângulo!')
