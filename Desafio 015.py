#Calculadora de aluguel de carro
print('Calcule o preço do aluguel do carro')
dias = int(input('Quantos dias o carro ficou alugado?'))
km = float(input('Quantos quilômetros rodados?'))
total = (dias*60)+(km*0.15)
print('Você vai pagar R${:.2f} pelo aluguel do carro'.format(total))