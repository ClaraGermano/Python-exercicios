# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.


palavra = ('MERCADO', 'LOJA', 'PROGRAMAR', 'FUTURO', 'APRENDER','PYTHON','PRATICAR','TRABALHAR')

for n in palavra:
    print(f'\nNa palavras {n} temos', end =' ')
    for letra in n:
        if letra in 'AEIOU':
            print(f'{letra.lower()}', end =' ')   #printando em minusculo

print('\n\033[33mFIM\033[m')




