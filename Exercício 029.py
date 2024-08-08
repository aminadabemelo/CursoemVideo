print('CALCULADORA DE MULTA')
velo = float(input('Digite a velocidade que você passou pelo radar: '))

if velo > 80:
    multa = (velo - 80) * 7
    print('Você foi multado!')
    print('A multa vai custar R$ {:.2f}'.format(multa))
else:
    print('Parabéns! Você não foi multado.')