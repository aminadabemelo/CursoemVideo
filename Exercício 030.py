numero = int(input('Digite um número inteiro para saber se ele par ou ímpar: '))
teste = numero % 2

if teste == 0:
    print('O número {} é par'.format(numero))
else:
    print('O número {} é ímpar'.format(numero))