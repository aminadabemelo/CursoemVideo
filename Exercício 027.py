nome = input('Digite o nome completo de uma pessoa: ').strip()
lista = nome.split()
tamlista = len(lista)

print('Primeiro nome: {}' .format(lista[0]))
print('Último nome: {}' .format(lista[tamlista - 1]))