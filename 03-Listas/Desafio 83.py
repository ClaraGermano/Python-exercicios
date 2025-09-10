# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.Seu aplicativo
# deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.


expressao = str(input('Digite uma expresão: '))
pilha = list()

for v in expressao:
    if v == '(':
        pilha.append('(')
    elif v == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('\033[1;34mSua expressão está correta!\033[m')
else:
    print('\033[1;31mSua expressão está incorreta!\033[m')