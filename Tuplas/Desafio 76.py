#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.


produto = (('Lápis',1.75,'Borracha',2.00,'Caderno',15.90,'Estojo',25.00,'Transferidor',4.20,'Compasso',
            9.00,'Mochila',120.32,'Canetas',22.30,'Livro',34.90))
print('\033[31m-\033[m'*40)
print(f'{'\033[1;33mLISTAGEM DE PREÇOS\033[m':^40}')
print('\033[31m-\033[m'*40)


for pos in range(0,len(produto),2):
    print(f'{produto[pos] :.<30}',end='')  #formatado: produto a esquerda
    print(f'R$ {produto[pos+1]:>5.2f}')     #formatado: produto a direita

#print((produto[n]),'........... R$' ,(produto[n]))
#print((produtos[0:1:2]),'........... R$',produtos[1:2:2])    #tentativas minhas
print('\033[31m-\033[m'*40)
