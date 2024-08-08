from datetime import date

print('Saiba a categoria do atleta pelo ano de nascimento')
ano_nasc = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - ano_nasc

if idade <= 9 and idade >= 0:
    print('Idade: {} anos \nCategoria: MIRIM'.format(idade))
elif idade > 9 and idade <= 14:
    print('Idade: {} anos \nCategoria: INFANTIL'.format(idade))
elif idade > 14 and idade <= 19:
    print('Idade: {} anos \nCategoria: JUNIOR'.format(idade))
elif idade > 19 and idade <= 20:
    print('Idade: {} anos \nCategoria: SÊNIOR'.format(idade))
elif idade > 20:
    print('Idade: {} anos \nCategoria: MASTER'.format(idade))
else:
    print('O atleta não nasceu ainda')