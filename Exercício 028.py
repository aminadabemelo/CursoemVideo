from random import randint
from time import sleep
numero = randint(0, 5)
print('O computador escolheu um número entre 0 a 5. Tente adivinhar!')
x = int(input('Digite o número: '))
print('PROCESSANDO...')
sleep(2)
if x == numero:
    print('Você acertou!')
else:
    print('Infelizmente você ERROU. O número certo é {}'.format(numero))
