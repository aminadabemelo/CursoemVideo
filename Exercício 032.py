from datetime import date
print('Descubra se qualquer ano foi ou é bissexto')
ano = int(input('Digite o ano ou 0 para o ano atual: '))
teste1 = ano % 4
teste2 = ano % 100
teste3 = ano % 400
if ano == 0:
    ano = date.today().year
if teste1 == 0 and teste2 != 0 or teste3 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
