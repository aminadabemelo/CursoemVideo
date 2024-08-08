#Verifica se tem Silva no nome
nome = input('Digite o nome completo de uma pessoa: ').strip()
capnome = nome.upper()
print('Esta pessoa tem Silva no nome: {}' .format('SILVA' in capnome))
