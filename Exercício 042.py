print('Descubra se os 3 segmentos de reta digitados formam um triângulo')
print('Caso positivo, saiba qual a classificação quanto aos lados')
print('Digite abaixo o comprimento de cada segmento abaixo')
r1 = int(input('r1: '))
r2 = int(input('r2: '))
r3 = int(input('r3: '))

if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
    if r1 == r2 and r1 == r3:
        print('As três retas podem formar um triângulo equilátero.')
    elif (r1 == r2 and r1 != r3) or (r1 == r3 and r1 != r2) or (r2 == r3 and r2 != r1):
        print('As três retas podem formar um triângulo isósceles.')
    else:
        print('As três retas podem formar um triângulo escaleno.')
else:
    print('As três retas não podem formar um triângulo')