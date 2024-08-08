#conversor de real p/ dólar
print('Conversor de Real(R$) em Dólar(US$)')
r = float(input('Digite o valor que você tem em reais:'))
p = 4.70
d = r/p
print('O preço do dólar está R${:.2f} \nVocê pode comprar US${:.2f}'.format(p, d))
