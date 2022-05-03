#Tratamento de erro incluso
from random import randint
from time import sleep
dicio = {
        'Kaio' : randint(1,20),
        'Sérgio' : randint(1,20),
        'Melyssa' : randint(1,20),
        'Alice' : randint(1,20)
        }
dicio_ordenado = dict()

for i in list(sorted(dicio.values(), reverse=True)):
    for k,v in dicio.items():
        if v == i:
            dicio_ordenado.update({k : v})

for k,v in dicio.items():
    print(f'O jogador {k} tirou {v}')
    sleep(0.5)

print('\n')

for k,v in enumerate(dicio_ordenado.items(), 1):
    print(f'{k}º lugar: {v[0]} com {v[1]}')