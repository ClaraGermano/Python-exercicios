#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o
# menor valor digitado e as suas respectivas posições na lista.

valores = list()

for p in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {p}: ')))

print('\033[33m=-=\033[m'*20)
print(f'Você digitou os valores {valores}')
maior = max(valores)
menor = min(valores)

print(f'O maior valor digitado foi {maior} nas posições: ',end=' ')
for i,v in enumerate (valores):
    if v == maior:
        print(f'{i}',end = '...')
print(f'\nO menor valor digitado foi {menor} nas posições: ',end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}',end ='...')


#print(valores.count(maior))
#print(f'O maior valor digitado foi {maior} na posição {valores.index(maior)}')
#print(f'O maior valor digitado foi {menor} na posição {valores.index(menor)}')
