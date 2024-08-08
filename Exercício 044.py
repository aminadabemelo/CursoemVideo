print('Preço do produto conforme forma de pagamento')
preco = float(input('Digite o preço do produto: R$ '))

pgto = int(input('Digite 1 para pagamento à vista ou 2 para cartão: '))

if pgto == 1:
    preco = preco * 0.9
    print('Você pagará R$ {:.2f} pelo produto'.format(preco))
elif pgto == 2:
    parcelas = int(input('Digite a quantidade de parcelas desejada: '))
    if parcelas == 1:
        preco = preco * 0.95
        print('Você pagará R$ {:.2f} pelo produto'.format(preco))
    elif parcelas == 2:
        print('Você pagará R$ {:.2f} pelo produto'.format(preco))
    elif parcelas >= 3:
        preco = preco * 1.2
        print('Você pagará R$ {:.2f} pelo produto'.format(preco))
else:
    print('Forma de pagamento inválida')