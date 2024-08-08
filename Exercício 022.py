#crie um progama que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas as letras minúsculas
#Quantas letras ao todo sem considerar os espaços
#Quantas letras tem o primeiro nome

nome = input('Digite o seu nome completo: ')
caract_sem = len(nome) - nome.count(' ')
pnome = len(nome[:nome.find(' ')])
print(nome.upper())
print(nome.lower())
print('O seu nome completo tem {} letras'.format(caract_sem))
print('O seu primeiro nome tem {} letras'.format(pnome))