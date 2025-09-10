# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.


n = int(input('Digite um número para ver sua tabuada:'))

print('\033[31m ## \033[m'*8)
print('\033[1;34m   TABUADA DE {} \033[m'.format(n))
print('\033[31m ## \033[m'*8)


for c in range(0,11):
    print( ' {} x {} = {}'.format( n , c , n * c))

