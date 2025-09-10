#07:Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

aluno = str(input('Nome do aluno: '))
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1+n2)/2
print('A média do(a) {:.1f} é {:.1f}'.format(aluno,media))