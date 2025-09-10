#Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma = 0
somater = 0
maiorvalor = ' '

for l in range (0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l},{c}]:'))

        if matriz[l][c] % 2 == 0:
            soma = soma + matriz[l][c]

        if c == 2:
            somater += matriz[l][c]

        if l == 1 and c == 0:
            maiorvalor = matriz[l][c]
        elif l == 1:
            if matriz[l][c] > maiorvalor:
                maiorvalor = matriz[l][c]


print('\033[31m=-=\033[m'*30)

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()

print('\033[31m=-=\033[m'*30)
print(f'A soma dos números pares é: {soma}')
print(f'A soma dos números na terceira coluna é: {somater}')
print(f'O maior valor da segunda linha é: {maiorvalor}')

# posso usar max para a letra c 