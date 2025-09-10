#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
#ESCALENO: todos os lados diferentes

a = float(input('Primeiro segmento:'))
b = float(input('Segundo seguimento:'))
c = float(input('Terceiro seguimento:'))

if a + b > c and a + c > b and b + c > a:
    print('Os seguimentos FORMAM um triângulo', end='')
    if a == b == c:
        print('\033[31m EQUILÁTERO ! \033[m', end='')
    elif a == b or a == c or b == c:
        print('\033[31m ISÓSCELES \033[m', end='')
    elif a != b and a != c and b != c:
        print('\033[31m ESCALENO! \033[m')          #poderia usar o else tbm e não precisar colocar toda a comparação
else:
    print('Os seguimentos NÃO formam um triângulo')



