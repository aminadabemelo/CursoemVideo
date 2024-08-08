#Unidade, dezena, centena, milhar
numero = input('Digite um número de 0000 a 9999: ')

print('Resolvendo como número')

x = int(numero)

print('unidade: {}'.format(x % 10))
print('dezena: {}' .format(x // 10 % 10))
print('centena: {}'.format(x //100 % 10))
print('milhar: {}' .format(x // 1000))