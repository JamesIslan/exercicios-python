# Tratamento de erro incluso
from math import sqrt
while True:
    global cat_oposto
    try:
        cat_oposto = float(input('Digite aqui o valor do cateto oposto: '))
        break
    except ValueError:
        print('Digite um valor válido!')
        continue

while True:
    global cat_adjacente
    try:
        cat_adjacente = float(input('Digite aqui o valor do cateto adjacente: '))
        break
    except ValueError:
        print('Digite um valor válido!')
        continue

hipotenusa = sqrt(((cat_adjacente ** 2) + (cat_oposto ** 2)))
print(f'A hipotenusa vale {float(hipotenusa)}')
