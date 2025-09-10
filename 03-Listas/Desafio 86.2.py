# Criando e preenchendo a matriz 3x3 direto
matriz = []  # lista vazia que vai receber as linhas

for l in range(3):
    linha = []  # lista que vai receber os elementos da linha
    for c in range(3):
        valor = int(input(f'Digite um valor para [{l},{c}]: '))
        linha.append(valor)  # adiciona o valor à linha
    matriz.append(linha)  # adiciona a linha completa à matriz

print('\033[31m=-=\033[m'*20)

# Mostrando a matriz
for linha in matriz:
    for valor in linha:
        print(f'[{valor:^5}]', end=' ')
    print()
