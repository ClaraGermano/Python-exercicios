#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.

'''print('\033[33m-=\033[m'*10)
print('\033[34m    Tabuada\033[m')
print('\033[33m-=\033[m'*10)

cont = 1
while True:
    n = int(input('Quer ver a tabuada de qual número?: '))
    if n < 0:
        break
    cont = 1     #reinicia o contador para cada novo número
    while cont <= 10:
        potencia = n * cont
        print(f'{n} x {cont} = {potencia}')
        cont = cont +1
print('Tabuada encerrada!Até a próxima! ')'''


print('\033[33m-=\033[m'*10)
print('\033[34m    Tabuada\033[m')
print('\033[33m-=\033[m'*10)

while True:
    n = int(input('Quer ver a tabuada de qual número?: '))
    print('\033[31m-\033[m'*30)
    if n < 0:
        break
    for c in range (1,11):
        print(f'{n} x {c} = {n * c}')
    print('\033[31m-\033[m'*30)
print('Tabuada encerrada! Até a próxima!! ')








