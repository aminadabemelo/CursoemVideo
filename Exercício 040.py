print('Calculadora de média')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2
""" 
Este programa considera notas maiores que 
6.9 e menores que 7 como aprovação e imprime 
estes valores arredondados para 7
"""
if media < 5:
    print('Sua média é {:.1f}, e infelizmente você foi REPROVADO'.format(media))
elif media >= 5 and media <= 6.9:
    print('Sua média é {:.1f}, e fará RECUPERAÇÃO'.format(media))
else:
    print('PARABÉNS, você foi APROVADO com média {:.1f}'.format(media))
