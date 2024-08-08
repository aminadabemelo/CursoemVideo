print('Descubra se 3 retas formam um triângulo')
print('Digite abaixo o comprimento de cada reta')
r1 = int(input('r1: '))
r2 = int(input('r2: '))
r3 = int(input('r3: '))

if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
    print('As três retas podem formar um triângulo!')
else:
    print('As três retas não podem formar um triângulo')