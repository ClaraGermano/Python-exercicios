#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na
#posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

#exercicio dificil

valor = list()

for p in range(0,5):
    v = int(input('Digite um valor: '))

    if p == 0:
        valor.append(v)
        print('\033[33mAdicionado no final da lista!\033[m')
    elif v >= valor[-1]:
        valor.append(v)       # o append sempre joga o valor no final da fila
        print('\033[33mValor adicionado no final da lista!\033[m')
    else:
        pos = 0
        while pos < len(valor):  #“Enquanto ainda existirem posições na lista para eu olhar, continua tentando achar o lugar certo.”
            if v <= valor[pos]:
                valor.insert(pos,v)
                print(f'\033[33mAdicionado na posição {pos} da lista\033[m')
                break
            pos += 1

print('\033[31m=-=\033[m'*30)
print(f'Os valores digitados em ordem foram: {valor}')


#obs:while pos < len(valor):
#pos = 0
#len(valor) = 2
#Como 0 < 2, o laço roda ✅