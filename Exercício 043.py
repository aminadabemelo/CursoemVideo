print('Calculadora de IMC')
peso = float(input('Digite o seu peso em quilogramas: '))
altura = float(input ('Digite a sua altura em metros: '))
imc = peso / altura**2

if imc < 18.5:
    print('Seu IMC é {:.1f} e você está abaixo do peso'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é {:.1f} e você está no peso normal'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é {:.1f} e você está com sobrepeso'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é {:.1f} e você está com obesidade'.format(imc))
else:
    print('Seu IMC é {:.1f} e você está com obesidade mórbida'.format(imc))