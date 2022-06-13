# Tratamento de erro incluso
from random import choices


def sorteia():
    sorteador = choices(range(1, 11), k=5)
    return sorteador


def somapar(var):
    pares = list(num for num in var if num % 2 == 0)
    somapares = sum(pares)
    dicio = {'pares': pares, 'somapares': somapares}
    return dicio


lista = sorteia()
soma_pares = somapar(lista)

print(f'Os números sorteados foram: {str(lista)[1:-1]}')
print(f'Os valores pares são: {soma_pares["pares"]} e a soma deles é {soma_pares["somapares"]}')
