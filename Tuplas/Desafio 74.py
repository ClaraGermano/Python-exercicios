#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
#mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.


from random import randint

#for cont in range(0,4):
#    computador = randint(0,10)
#    print(f'Os valores sorteados foram: {computador}')


computador = (randint(0,10), randint(0,10), randint(0,10),randint(0,10),randint(0,10))

#print(f'Os valores sorteados foram: {computador}')    #outra forma de mostar os valores
for n in computador:
   print(f'{n} ', end='')   #outra forma de mostrar os valores
print(f'\nO maior valor foi {max(computador)}')
print(f'O menor valor foi {min(computador)}')
