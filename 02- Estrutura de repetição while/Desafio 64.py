#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
#o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma
#entre eles (desconsiderando o flag).


soma = 0
n = 0              # soma = n = cont = 0
cont = 0
while n != 999:
    n = int(input('Digite um número\033[31m[cod 999 para parar]\033[m:'))
    if n != 999:
        soma = soma + n
        cont += 1

print('Você digitou {} números. A soma dos números é {}'.format(cont,soma))



# jeito Prof

'''n = int(input('Digite um número [999 para parar]: '))  # ← primeira leitura
soma = cont = 0

while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número [999 para parar]: '))  # ← segunda leitura
print('Você digitou {} números. A soma dos números é {}'.format(cont,soma))'''