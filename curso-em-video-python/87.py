# Tratamento de erro incluso
lista = []

for i in range(3):
    while len(lista) != 3:
        try:
            lista += \
                [[
                    int(input('Digite um valor numérico: ')),
                    int(input('Digite um valor numérico: ')),
                    int(input('Digite um valor numérico: '))
                ]]
        except ValueError:
            print('Digite um valor válido!')
            continue
    print('\n', *list([num] for num in lista[i]), sep=' ')

print(f'\nA soma dos valores pares digitados é: '
      f'{sum((num for num in (*lista[0], *lista[1], *lista[2]) if num % 2 == 0))}')

print(f'\nA soma dos valores da terceira coluna é: '
      f'{sum(num for num in lista[2])}')

print(f'\nO maior valor da segunda linha é: '
      f'{max(lista[1])}')