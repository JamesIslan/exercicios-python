# Tratamento de erro incluso
import random

aluno1 = "Garibaldo"
aluno2 = "Adamastor"
aluno3 = "Adonias"
aluno4 = "Valtemário"
aluno_escolhido = random.randint(1, 4)
if aluno_escolhido == 1:
    print(f'O aluno escolhido foi {aluno1}')
if aluno_escolhido == 2:
    print(f'O aluno escolhido foi {aluno2}')
if aluno_escolhido == 3:
    print(f'O aluno escolhido foi {aluno3}')
if aluno_escolhido == 4:
    print(f'O aluno escolhido foi {aluno4}')
