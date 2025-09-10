#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

tupla = ('zero','um', 'dois', 'três','quatro','cinco','seis','sete','oito','nove',
        'dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

n = int(input('Digite um número entre 0 e 20:'))

while n > 20 or n < 0 :
    n = int(input('Tente novamente! digite um número entre 0 e 20: '))

print(f'Você digitou o número \033[31m{tupla[n]}\033[m!')

