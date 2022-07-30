import random
aluno1 = input('Digite aqui o nome do primeiro aluno: ')
aluno2 = input('Digite aqui o nome do segundo aluno: ')
aluno3 = input('Digite aqui o nome do terceiro aluno: ')
aluno4 = input('Digite aqui o nome do quarto aluno: ')
aluno5 = input('Digite aqui o nome do quinto aluno: ')
lista_alunos = [aluno1, aluno2, aluno3, aluno4, aluno5]
random.shuffle(lista_alunos)
print(lista_alunos)
