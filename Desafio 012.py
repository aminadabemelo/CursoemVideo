#Calculadora de desconto
print('calculadora de preço com desconto')
p = float(input('Digite o valor do produto: R$'))
d = float(input('Digite a porcentagem do desconto (sem o %):'))
t = p-(p*(d/100))
print('O preço com desconto de {:.1f}% é: R${:.2f}'.format(d, t))