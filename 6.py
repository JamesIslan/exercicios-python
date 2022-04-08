# Tratamento de erro incluso
from math import sqrt
numero = int()
while True:
    try:
        numero = int(input('Digite aqui um número inteiro: '))
    except ValueError:
        print('Digite apenas números inteiros!')
        continue
    dobro = numero * 2
    triplo = numero * 3
    raiz_quadrada = sqrt(numero)
    print(f'O dobro de {numero} é {dobro}, o triplo de {numero} é {triplo} '
          f'e a raíz quadrada de {numero} é {raiz_quadrada:.5f}')
