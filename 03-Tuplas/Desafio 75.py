# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.



n = (int(input('Digite um número:')),int(input('Digite outro número:')),
     int(input('Digite mais número:')),int(input('Digite o último número número:')))
print('=-='*20)
print(f'Você digitou os números: {n}')
print(f'O número 9 aparece: {n.count(9)} vezes')
if 3 in n:
     print(f'O primeiro número 3 foi digitado na posição {n.index(3)+1}°')
else:
     print('O valor 3 não foi digitado em nenhuma posição')

print('Os valores pares digitados foram', end=' ')
for cont in n:
     if cont % 2 == 0:
          print(cont , end=' ')