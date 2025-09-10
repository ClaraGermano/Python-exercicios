# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. Exemplos de palíndromos:
# APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.



'''frase = str(input('Digite uma frase: ')).strip().upper() #eliminou espaço antes e depois e jogou para maisculo
palavra = frase.split()  #separou em palavras
junto = ''.join(palavra)  #juntou tudo em uma frase só
inverso = ''
for letra in range (len(junto)-1, -1 , -1):   #inicio, fim, pulando. -1 significa que começa no final. -1 de tras pra frente
    inverso = inverso + junto[letra]
print('O inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase não é um palíndromo')'''

# outra forma, sem usar for, com tecnica de fatiamento



frase = str(input('Digite uma frase: ')).strip().upper() #eliminou espaço antes e depois e jogou para maisculo
palavra = frase.split()  #separou em palavras
junto = ''.join(palavra)  #juntou tudo em uma frase só
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase não é um palíndromo')






