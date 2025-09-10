#11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinha
#necessária para pinta-lá, sabendo que cada litro de tinta, pinta uma área de 2m²

print('Calcule aqui a quantidade de tinta necessária para pintar a parede:')
largura = float(input('Largura da parede em metros:'))
altura = float(input('Altura da parede em metros:'))
area = largura*altura
tinta = area/2
print('A área da parede é {}m², vai ser necessário {}l para pintar a parede'.format(area,tinta))
