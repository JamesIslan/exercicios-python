from math import sqrt
cat_oposto = float(input('Digite aqui o valor do cateto oposto: '))
cat_adjacente = float(input('Digite aqui o valor do cateto adjacente: '))
hipotenusa = sqrt(((cat_adjacente ** 2) + (cat_oposto ** 2)))
print(f'A hipotenusa vale {float(hipotenusa)}')