#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
#qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

print('\033[36m -#- \033[m' * 8)
print('\033[31m  Conversor de Bases Numéricas \033[m ')
print('\033[36m -#- \033[m' * 8)

num = int(input('Escreva um número inteiro:'))
print('Escolha uma das bases para conversão:')
print('[ 1 ] Converter para BINÁRIO ')
print('[ 2 ] Converter para OCTAL')
print('[ 3 ] Converter para HEXADECIMAL')

base = int(input('Sua opção:'))

if base == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format(num,bin(num)[2:]))
elif base == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num,oct(num)[2:]))
elif base == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num,hex(num)[2:]))
else:
    print('\033[1;31m Opção inválida.Tente novamente \033[m')



