#Calculadora de aumento de salário
print('calculadora de aumento de salário')
s = float(input('Digite o valor do salário: R$'))
a = float(input('Digite a porcentagem do aumento (sem o %):'))
t = s+(s*(a/100))
print('O salário com aumento de {:.1f}% é: R${:.2f}'.format(a, t))