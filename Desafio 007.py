#Calculadora de média
nome = input('Digite o seu nome:')
print('Olá {}, vamos calcular a sua média!'.format(nome))
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
n3 = float(input('Digite a terceira nota:'))
media = (n1+n2)/3
print('A sua média é: {:.1f}'.format(media))