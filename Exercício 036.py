from time import sleep
print('Silumador de programa habitacional')
preco = float(input('Qual o valor do imóvel? '))
salario = float(input('Qual a sua renda mensal? '))
anos = int(input('Em quantos anos você quer pagar? '))

tempo = anos * 12
parcela = preco / tempo
margem = salario * 0.3

print('=' * 45)
print('AVISO IMPORTANTE!!!')
print('A parcela só pode ser até 30% da sua renda')
print('=' * 45)
sleep(2)
print('PROCESSANDO SIMULAÇÃO...')
sleep(3)

if parcela <= margem:
    print('Parabéns! O seu emprestimo pode ser aprovado.')
    print('Margem: R$ {:.2f}'.format(margem))
    print('Valor do imóvel: R$ {:.2f}'.format(preco))
    print('Tempo: {} meses'.format(tempo))
    print('Parcelas: R$ {:.2f}'.format(parcela))
else:
    print('Infelizmente esse tempo para pagamento excede a sua margem.')
    print('Margem: {}'.format(margem))
    print('Parcelas: R$ '.format(parcela))
    print('EMPRESTIMO NEGADO')