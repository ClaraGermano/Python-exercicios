# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

nome = str(input('Qual o nome da Cidade que você nasceu?')).strip() #tirando os espaços
print(nome[:5].upper() == 'SANTO')  #Verificando as 5 letras, jogando sempre para maiuscula
