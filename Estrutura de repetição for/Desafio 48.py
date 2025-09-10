# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.

print('\033[33m-*-\033[m' *8)
print('  \033[31m CONTANDO \033[m ')
print('\033[33m-*-\033[m' *8)
soma = 0
cont = 0
for n in range (1 , 501, 2):
    if n % 3 == 0:
        cont = cont +1                 #contador
        soma = soma + n               #acumulador
print('A soma dos {} números ímpares que são multiplos de 3 é {}'.format (cont, soma))
