from random import shuffle

print ('Vamos sortear a sequência de alunos para apresentação dos trabalhos')

a1 = input('Nome do aluno 1:')
a2 = input('Nome do aluno 2:')
a3 = input('Nome do aluno 3:')
a4 = input('Nome do aluno 4:')

lista = [a1, a2, a3, a4]
shuffle(lista)

print('A sequência de apresentação é: \n{}' .format(lista))
