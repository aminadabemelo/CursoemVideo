from math import hypot

print('Vamos calcular a hipotenusa de um triângulo retângulo')

catoposto = float(input('Digite o valor do cateto oposto:'))
catadjacente = float(input('Digite o valor do cateto adjacente:'))
hipotenusa = hypot(catoposto, catadjacente)

print('A hipotenusa do triângulo retângulo é: {:.2f}' .format(hipotenusa))