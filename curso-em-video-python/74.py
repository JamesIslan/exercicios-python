from random import randint as aleatorio
numeros = (
    aleatorio(
        0, 100), aleatorio(
            0, 100), aleatorio(
                0, 100), aleatorio(
                    0, 100), aleatorio(
                        0, 100))
print(f'Os números gerados foram {numeros}')
print(
    f'O maior valor da lista é {max(numeros)} e o menor valor é {min(numeros)}')
