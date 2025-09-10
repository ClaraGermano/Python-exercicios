# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.



#for n in range (1,51):
#    if n % 2 == 0:
#        print(n , end = ' ')


for n in range (2,51,2):
    if n % 2 == 0:               #vai mostrar mesmo resultado, mas com menos iteraçoes, ocupando menos
        print(n , end = ' ')


# coloque print('.', end = '')   pra conseguir ver a iteração