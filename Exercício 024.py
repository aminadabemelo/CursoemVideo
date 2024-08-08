#Verifica de há SANTO no nome da cidade
cidade = input('Digite o nome de uma cidade: ').strip()
pnome = cidade[:cidade.find(' ')]
cappnome = pnome.upper()
print('O nome da cidade começa com Santo: {}' .format('SANTO' in cappnome))
