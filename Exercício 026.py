#Verifica as letras 'A' na frase
frase = input('Digite uma frase: ').strip()
upfrase = frase.upper()
qtd = upfrase.count('A')
invert = upfrase[::-1]
print('A letra "A" aparece {} vezes nesta frase' .format(qtd))
print('A letra "A" aparace a primeira vez na posição {}' .format(upfrase.find('A') + 1))
print('A letra "A" aparece pela ultima vez na posição {}' .format(upfrase.rfind('A') + 1))
