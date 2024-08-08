print('Qual dos 3 números é o maior e qual é o menor?')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
maior = 0
menor = 0

if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1
if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3

print('O maior dos números é o {}'.format(maior))
print('O menor dos números é o {}'.format(menor))
