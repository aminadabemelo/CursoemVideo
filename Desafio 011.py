# Calculadora de área da parede e quantidade de tinta
print('Vamos saber quantos litros de tinta você precisa para pintar uma parede!')
a = float(input('Digite a altura da sua parede em metros:'))
l = float(input('Agora a largura também em metros:'))
m = a*l
q = m/2
print('A sua parede tem {:.2f} m² \nVocê vai precisar de {:.2f} litros de tinta para pintar a sua parede'.format(m, q))
