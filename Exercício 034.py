print('Calculo de aumento de salário')
salario = float(input('Digite o valor do seu salário: '))

if salario > 1250:
    salario2 = salario * 1.1
    print('Seu salário será R$ {:.2f}'.format(salario2))
else:
    salario2 = salario * 1.15
    print('Seu salário será R$ {:.2f}'.format(salario2))