print('Calculadora de preço de passagem')
km = float(input('Digite a distância da sua viagem em quilômetros: '))

if km <= 200:
    preco = km * 0.5
    print('O preço da passagem é R$ {:.2f}'.format(preco))
else:
    preco = km * 0.45
    print('O preço da passagem é R$ {:.2f}'.format(preco))